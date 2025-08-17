import datetime as dt
import os
import re
from pathlib import Path
from typing import Any

import yaml
from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv
from loguru import logger
from openai import APIConnectionError, BadRequestError, RateLimitError

try:
    from crewai import agent, crew, task
except Exception:
    agent = task = crew = lambda x: x

from crewai_tools import GithubSearchTool, SerperDevTool

from src.openai_client import client as openai_client


def _read_yaml(path: Path) -> dict[str, Any]:
    """Les YAML og returner dict; feil hvis filen ikke finnes."""
    if not path.exists():
        raise FileNotFoundError(f"YAML ikke funnet: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-") or "rapport"


class DeepResearchCrew:
    def __init__(self, research_topic: str):
        load_dotenv()
        self.research_topic = research_topic.strip() or "agentic ai trender 2025"
        self.openai_model = os.getenv("OPENAI_MODEL_NAME", os.getenv("MODEL", "gpt-4o"))

        # Verktøy: Serper er valgfritt (kun hvis SERPER_API_KEY finnes)
        self.serper_tool = SerperDevTool() if os.getenv("SERPER_API_KEY") else None
        self.github_tool = GithubSearchTool()

        base = Path(__file__).parent
        agents_cfg = _read_yaml(base / "agents.yaml")
        tasks_cfg = _read_yaml(base / "tasks.yaml")

        self.agents = {a.get("name"): a for a in agents_cfg.get("agents", [])}
        self.tasks = {t.get("name"): t for t in tasks_cfg.get("tasks", [])}

        if "deep_research_agent" not in self.agents:
            raise KeyError("agents.yaml mangler agent med name: deep_research_agent")
        if "deep_research_task" not in self.tasks:
            raise KeyError("tasks.yaml mangler task med name: deep_research_task")

        logger.remove()
        logger.add(lambda m: print(m, end=""), level=os.getenv("LOG_LEVEL", "INFO"))

    def _render(self, s: Any) -> Any:
        return s.replace("{{ research_topic }}", self.research_topic) if isinstance(s, str) else s

    @agent
    def deep_research_agent(self) -> Agent:
        cfg = self.agents["deep_research_agent"]
        tools = [t for t in (self.serper_tool, self.github_tool) if t]
        return Agent(
            role=cfg.get("role", "Deep Research Leader"),
            goal=cfg.get("goal", "Dyp forskning og syntese"),
            backstory=cfg.get("backstory", ""),
            tools=tools,
            allow_delegation=cfg.get("allow_delegation", True),
            verbose=True,
            llm=cfg.get("llm", self.openai_model),
            temperature=cfg.get("temperature", 0.2),
        )

    @task
    def deep_research_task(self) -> Task:
        cfg = self.tasks["deep_research_task"]
        return Task(
            description=self._render(cfg.get("description", "")),
            expected_output=self._render(cfg.get("expected_output", "")),
            agent=self.deep_research_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.deep_research_agent()],
            tasks=[self.deep_research_task()],
            process=Process.sequential,
            verbose=True,
            memory=True,
        )

    def generate_report(self, prompt: str) -> str:
        """Kall LLM og skriv rapport til outputs/, returner absolutt filsti."""
        system_msg = (
            "Du er en senioranalytiker. Skriv en strukturert forskningsrapport i Markdown "
            "med kilder (lenker), analyse, risiko og anbefalinger."
        )
        try:
            r = openai_client.chat.completions.create(
                model=self.openai_model,
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
            )
            content = r.choices[0].message.content

            outdir = Path("outputs")
            outdir.mkdir(parents=True, exist_ok=True)

            ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
            topic_slug = _slugify(self.research_topic)[:60]
            path = outdir / f"{topic_slug}_report_{ts}.md"
            path.write_text(content, encoding="utf-8")
            return str(path.resolve())

        except (APIConnectionError, RateLimitError, BadRequestError) as e:
            logger.error(f"OpenAI API error: {e}")
            raise
