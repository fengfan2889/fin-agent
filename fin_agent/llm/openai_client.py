from openai import OpenAI
from fin_agent.llm.base import LLMBase

class OpenAICompatibleClient(LLMBase):
    def __init__(self, api_key, base_url, model):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = model

    def chat(self, messages, tools=None, tool_choice=None):
        """
        Send a chat completion request to an OpenAI-compatible API.
        """
        params = {
            "model": self.model,
            "messages": messages,
        }
        
        if tools:
            params["tools"] = tools
        if tool_choice:
            params["tool_choice"] = tool_choice

        try:
            response = self.client.chat.completions.create(**params)
            return response.choices[0].message
        except Exception as e:
            print(f"Error calling LLM API: {e}")
            raise e

