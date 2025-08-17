# scripts/gen_report.py
from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

from src.crew import DeepResearchCrew


def main(argv: list[str] | None = None) -> int:
    """Generer en rapport for gitt topic (argv) og skriv sti til stdout."""
    load_dotenv()

    args = argv if argv is not None else sys.argv[1:]
    topic = " ".join(args) if args else "agentic ai trender 2025"

    logger.info(f"Kjører DeepResearch på: {topic}")
    drc = DeepResearchCrew(research_topic=topic)

    result = drc.crew().kickoff(inputs={"research_topic": topic})
    result_str = str(result) if result is not None else ""

    prompt = (
        f"Emne: {topic}\n"
        "Oppgave: Oppsummer funnene til en helhetlig rapport med kilder, "
        "analyse, risiko og anbefalinger.\n"
        "Funn:\n"
        f"{result_str}\n"
    )

    out_path = Path(drc.generate_report(prompt)).resolve()
    print(f"Rapport: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
