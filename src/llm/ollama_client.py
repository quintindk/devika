import httpx
from ollama import Client

from src.logger import Logger
from src.config import Config

class Ollama:
    def __init__(self, ollama_url: str = None):
        config = Config()
        api_key = config.get_openai_api_key()
        self.client = OAI(
            api_key=api_key,
        )

    def list_models(self):
        try:
            return self.client.list()["models"]
        except httpx.ConnectError:
            Logger().warning("Ollama server not running, please start the server to use models from Ollama.")
        except Exception as e:
            Logger().error(f"Failed to list Ollama models: {e}")

        return []

    def inference(self, model_id: str, prompt: str) -> str:
        response = self.client.generate(
            model = model_id,
            prompt = prompt.strip()
        )

        return response['response']
