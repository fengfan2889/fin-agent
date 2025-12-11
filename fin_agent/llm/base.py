from abc import ABC, abstractmethod

class LLMBase(ABC):
    @abstractmethod
    def chat(self, messages, tools=None, tool_choice=None):
        """
        Send a chat completion request to the LLM.
        
        :param messages: List of message dictionaries (role, content).
        :param tools: List of tool definitions (optional).
        :param tool_choice: Tool choice strategy (optional).
        :return: The response message object (content, tool_calls, etc.).
        """
        pass

