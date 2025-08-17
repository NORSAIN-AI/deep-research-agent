import os

from dotenv import load_dotenv

# Last inn .env hvis den finnes
load_dotenv()

# Sett trygge default-verdier lokalt (overskrives i CI av GitHub Secrets)
os.environ.setdefault("OPENAI_API_KEY", "local-test-key")
os.environ.setdefault("SERPER_API_KEY", "local-test-key")
