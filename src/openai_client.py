# src/openai_client.py
import logging
import os
import sys

from openai import OpenAI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_client() -> OpenAI:
    """
    Return an OpenAI client configured with API key from environment.
    Exits with error if OPENAI_API_KEY is missing.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit(
            "❌ OPENAI_API_KEY is not set. Please configure your environment or GitHub Secret."
        )
    logger.info("✅ OpenAI client initialized with API key from environment")
    return OpenAI(api_key=api_key)


def get_client_with_key(api_key: str) -> OpenAI:
    """
    Return an OpenAI client configured with the provided API key.
    Exits with error if key is missing.
    """
    if not api_key:
        sys.exit("❌ API key is not provided. Please provide a valid OpenAI API key.")
    logger.info("✅ OpenAI client initialized with provided API key")
    return OpenAI(api_key=api_key)


# Shared client for general use
client: OpenAI = get_client()


def get_shared_client() -> OpenAI:
    """
    Return the shared OpenAI client.
    """
    return client
