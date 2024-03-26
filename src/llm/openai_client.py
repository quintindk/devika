from openai import OpenAI as OAI

from src.config import Config

class OpenAI:
    def __init__(self):
        config = Config()
        endpoint = config.get_openai_url()
        api_key = config.get_openai_api_key()
        self.client = OAI(
            base_url=endpoint,
            api_key=api_key,
        )
        
    def inference(self, model_id: str, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt.strip(),
                }
            ],
            model=model_id,
        )

        return chat_completion.choices[0].message.content
