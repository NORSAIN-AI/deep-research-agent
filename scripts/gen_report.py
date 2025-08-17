#!/usr/bin/env python3
"""
Generate research report with DeepResearchCrew.
Usage:
    python scripts/gen_report.py "ditt tema her"
"""

import argparse
import logging
import sys
from pathlib import Path

from src.crew import DeepResearchCrew

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a research report with DeepResearchCrew."
    )
    parser.add_argument(
        "topic",
        nargs="*",
        help="Research topic (default: 'agentic ai trender 2025')",
    )
    args = parser.parse_args()

    topic = " ".join(args.topic) if args.topic else "agentic ai trender 2025"
    logging.info(f"Starter DeepResearchCrew for tema: {topic}")

    try:
        crew = DeepResearchCrew(research_topic=topic)
        res = crew.crew().kickoff(inputs={"research_topic": topic})

        report_content = f"# Funn\n\n{res}"
        path = crew.generate_report(report_content)

        logging.info("✅ Rapport generert")
        print(f"📄 Rapport lagret: {Path(path).absolute()}")

    except Exception as e:
        logging.error(f"Feil under generering: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
