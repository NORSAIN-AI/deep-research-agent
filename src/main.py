import sys
from loguru import logger
from dotenv import load_dotenv
from src.crew import DeepResearchCrew

def main():
    load_dotenv()
    topic = "agentic ai trender 2025" if len(sys.argv)==1 else " ".join(sys.argv[1:])
    logger.info(f"Kjører DeepResearch på: {topic}")
    drc = DeepResearchCrew(research_topic=topic)
    result = drc.crew().kickoff(inputs={"research_topic": topic})
    prompt = f"""Emne: {topic}
Oppgave: Oppsummer funnene til en helhetlig rapport med kilder, analyse, risiko og anbefalinger.
Funn:
{result}
"""
    out = drc.generate_report(prompt)
    print("\n=== Rapport lagret i ===\n", out)

if __name__ == "__main__":
    main()
