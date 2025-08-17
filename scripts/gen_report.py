from src.crew import DeepResearchCrew
import sys
topic = " ".join(sys.argv[1:]) if len(sys.argv)>1 else "agentic ai trender 2025"
crew = DeepResearchCrew(research_topic=topic)
res = crew.crew().kickoff(inputs={"research_topic": topic})
path = crew.generate_report(f"Funn:\n{res}")
print("Rapport:", path)
