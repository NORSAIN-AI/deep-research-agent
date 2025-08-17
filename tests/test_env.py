import os

import pytest


def test_openai_key_is_set() -> None:
    if "OPENAI_API_KEY" not in os.environ:
        pytest.skip("OPENAI_API_KEY not set")
    assert True


def test_env() -> None:
    if "OPENAI_API_KEY" not in os.environ:
        pytest.skip("OPENAI_API_KEY not set")
    # SERPER kan være valgfritt – bare sjekk hvis du krever det
    assert True
