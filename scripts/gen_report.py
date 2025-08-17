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

from src.crew import DeepResearchCrew  # forutsetter at src/crew.py finnes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def main() -> int:
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
    logging.info(f"Starter DeepResearchCrew for tema: {topic!r}")

    try:
        crew = DeepResearchCrew(research_topic=topic)

        # Kickoff workflow
        result = crew.crew().kickoff(inputs={"research_topic": topic})

        # Bygg rapportinnhold (Markdown)
        report_md = f"# Rapport: {topic}\n\n## Funn\n{result}\n"

        # Generer og lagre rapport via din crew-implementasjon
        path = crew.generate_report(report_md)

        abs_path = Path(path).resolve()
        logging.info("✅ Rapport generert")
        print(f"📄 Rapport lagret: {abs_path}")
        return 0

    except Exception as e:
        logging.error(f"❌ Feil under generering: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
