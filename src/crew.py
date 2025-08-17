import os, datetime, yaml
from dotenv import load_dotenv
from loguru import logger
from openai import OpenAI
from crewai import Agent, Task, Crew, Process
try:
    from crewai import agent, task, crew
except Exception:
    agent = task = crew = lambda x: x
from crewai_tools import SerperDevTool, GithubSearchTool

class DeepResearchCrew:
    def __init__(self, research_topic: str):
        load_dotenv()
        self.research_topic = research_topic
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.openai_model = os.getenv("OPENAI_MODEL_NAME", os.getenv("MODEL", "gpt-4o"))
        self.serper_tool = SerperDevTool()
        self.github_tool = GithubSearchTool()
        base = os.path.dirname(__file__)
        self.agents = {a.get("name"): a for a in yaml.safe_load(open(os.path.join(base,"agents.yaml"), encoding="utf-8")).get("agents",[])}
        self.tasks = {t.get("name"): t for t in yaml.safe_load(open(os.path.join(base,"tasks.yaml"), encoding="utf-8")).get("tasks",[])}
        logger.remove(); logger.add(lambda m: print(m, end=""), level=os.getenv("LOG_LEVEL","INFO"))

    def _render(self, s:str)->str:
        return s.replace("{{ research_topic }}", self.research_topic) if isinstance(s,str) else s

    @agent
    def deep_research_agent(self)->Agent:
        cfg = self.agents.get("deep_research_agent", {})
        return Agent(
            role=cfg.get("role","Deep Research Leader"),
            goal=cfg.get("goal","Dyp forskning og syntese"),
            backstory=cfg.get("backstory",""),
            tools=[self.serper_tool, self.github_tool],
            allow_delegation=cfg.get("allow_delegation", True),
            verbose=True,
            llm=cfg.get("llm", self.openai_model),
            temperature=cfg.get("temperature", 0.2),
        )

    @task
    def deep_research_task(self)->Task:
        cfg = self.tasks.get("deep_research_task", {})
        return Task(
            description=self._render(cfg.get("description","")),
            expected_output=self._render(cfg.get("expected_output","")),
            agent=self.deep_research_agent(),
        )

    @crew
    def crew(self)->Crew:
        return Crew(
            agents=[self.deep_research_agent()],
            tasks=[self.deep_research_task()],
            process=Process.sequential,
            verbose=True,
            memory=True,
        )

    def generate_report(self, prompt:str)->str:
        system_msg = "Du er en senioranalytiker. Skriv en strukturert forskningsrapport i Markdown med kilder (lenker), analyse, risiko og anbefalinger."
        r = self.openai_client.chat.completions.create(model=self.openai_model, messages=[
            {"role":"system", "content":system_msg},
            {"role":"user", "content":prompt},
        ])
        content = r.choices[0].message.content
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        os.makedirs("outputs", exist_ok=True)
        path = f"outputs/research_report_{ts}.md"
        open(path,"w",encoding="utf-8").write(content)
        return path
