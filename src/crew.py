import os
import re
import datetime as dt
from pathlib import Path
from typing import Any, Dict

from dotenv import load_dotenv
from loguru import logger
import yaml
from openai import APIConnectionError, RateLimitError, BadRequestError

from crewai import Agent, Task, Crew, Process
try:
    from crewai import agent, task, crew
except Exception:
    agent = task = crew = lambda x: x

from crewai_tools import SerperDevTool, GithubSearchTool
from src.openai_client import client as openai_client


def _read_yaml(path: Path) -> Dict[str, Any]:
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
        self.openai_model = os.getenv("OPENAI_MODEL_NAME", os.getenv("MODEL", "gpt-4o")
                                      )
        self.serper_tool = SerperDevTool()
        self.github_tool = GithubSearchTool()
        base = Path(__file__).parent
        agents_cfg = _read_yaml(base / "agents.yaml")
        tasks_cfg = _read_yaml(base / "tasks.yaml")
        self.agents = {a.get("name"): a for a in agents_cfg.get("agents", [])}
        self.tasks = {t.get("name"): t for t in tasks_cfg.get("tasks", [])}
        if "deep_research_agent" not in self.agents:
            raise KeyError(
                "agents.yaml mangler agent med name: deep_research_agent")
        if "deep_research_task" not in self.tasks:
            raise KeyError(
                "tasks.yaml mangler task med name: deep_research_task")
        logger.remove()
        logger.add(lambda m: print(m, end=""),
                   level=os.getenv("LOG_LEVEL", "INFO"))

    def _render(self, s: Any) -> Any:
        if isinstance(s, str):
            return s.replace("{{ research_topic }}", self.research_topic)
        return s

    @agent
    def deep_research_agent(self) -> Agent:
        cfg = self.agents["deep_research_agent"]
        return Agent(
            role=cfg.get("role", "Deep Research Leader"),
            goal=cfg.get("goal", "Dyp forskning og syntese"),
            backstory=cfg.get("backstory", ""),
            tools=[self.serper_tool, self.github_tool],
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
            )
            content = r.choices[0].message.content
            ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
            os.makedirs("outputs", exist_ok=True)
            path = f"outputs/research_report_{ts}.md"
            open(path, "w", encoding="utf-8").write(content)
            return path
        except (APIConnectionError, RateLimitError, BadRequestError) as e:
            logger.error(f"OpenAI API error: {e}")
            return str(e)
