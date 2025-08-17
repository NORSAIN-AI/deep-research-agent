# src/main.py
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

from src.crew import DeepResearchCrew


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Kjør DeepResearch og generér en Markdown-rapport.")
    p.add_argument(
        "topic",
        nargs="*",
        help="Tema for research (default: 'agentic ai trender 2025')",
    )
    p.add_argument(
        "--log-level",
        default=os.getenv("LOG_LEVEL", "INFO"),
        help="Loggnivå (DEBUG, INFO, WARNING, ERROR). Default: %(default)s",
    )
    return p.parse_args()


def ensure_env() -> None:
    """Valider at nødvendige nøkler finnes i miljøet."""
    missing = []
    if not os.getenv("OPENAI_API_KEY"):
        missing.append("OPENAI_API_KEY")
    # SerperDevTool trenger denne hvis den brukes i oppsettet ditt:
    if os.getenv("USE_SERPER", "1") not in ("0", "false", "False") and not os.getenv(
        "SERPER_API_KEY"
    ):
        missing.append("SERPER_API_KEY (kreves av SerperDevTool)")
    if missing:
        msg = "❌ Mangler miljøvariabler: " + ", ".join(missing)
        raise OSError(msg)


def main() -> int:
    load_dotenv()
    args = parse_args()

    # konfigurer loguru
    logger.remove()
    logger.add(sys.stderr, level=args.log_level, enqueue=True, backtrace=False, diagnose=False)

    topic = " ".join(args.topic) if args.topic else "agentic ai trender 2025"
    logger.info(f"🚀 Starter DeepResearch for tema: '{topic}'")

    try:
        ensure_env()
    except OSError as e:
        logger.error(str(e))
        return 2

    start = time.time()
    try:
        drc = DeepResearchCrew(research_topic=topic)

        # kjør workflow
        result = drc.crew().kickoff(inputs={"research_topic": topic})

        # bygg prompt for rapporten
        prompt = (
            f"Emne: {topic}\n"
            "Oppgave: Oppsummer funnene til en helhetlig rapport med kilder, analyse, risiko og anbefalinger.\n"
            "Funn:\n"
            f"{result}\n"
        )

        out_path = Path(drc.generate_report(prompt)).resolve()
        elapsed = time.time() - start

        logger.info(f"✅ Ferdig på {elapsed:.1f}s")
        print("\n=== Rapport lagret i ===")
        print(out_path)
        return 0

    except KeyboardInterrupt:
        logger.warning("Avbrutt av bruker (Ctrl+C).")
        return 130
    except Exception as e:
        logger.exception(f"Uventet feil: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
