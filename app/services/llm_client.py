
from google import genai

from app.config import GOOGLE_API_KEY, LLM_MODEL


class GeminiClient:

    def __init__(self):
        if not GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY is not configured. "
                "Add it to your .env file."
            )

        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        self.model = LLM_MODEL

    def generate(self, prompt: str) -> str:

        models_to_try = [
            self.model,
            "gemini-3.5-flash-lite",
        ]

        last_error = None

        for model_name in models_to_try:

            try:
                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt,
                )

                if response.text:
                    return response.text

            except Exception as exc:
                last_error = exc

        raise RuntimeError(
            f"LLM request failed for all configured models. "
            f"Last error: {last_error}"
        )

