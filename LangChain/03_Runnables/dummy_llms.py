from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class DummyLlm:

    def __init__(self, model=None):
        """
        model : Any LangChain chat model.

        If no model is provided,
        ChatOpenAI() will be used.
        """

        if model is None:
            model = ChatOpenAI()

        self.model = model

    def predict(self, prompt):

        # Validation 1
        if not isinstance(prompt, str):
            raise TypeError(
                f"Prompt must be a string. Got {type(prompt).__name__}"
            )

        # Validation 2
        if prompt.strip() == "":
            raise ValueError(
                "Prompt cannot be empty."
            )

        response = self.model.invoke(prompt)

        return response.content