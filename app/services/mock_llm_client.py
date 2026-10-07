class MockLLMClient:
    """
    Fake LLM client used for local testing.

    It returns a predefined response so tests don't require
    an external API call.
    """

    def __init__(self, response: str):
        self.response = response

    def generate(self, prompt: str) -> str:
        return self.response