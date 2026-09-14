from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool, StructuredTool
from pydantic import BaseModel, Field

load_dotenv()


# ------------------ Tool Input Schema ------------------
class MultiplyInput(BaseModel):
    a: float = Field(description="This is the first number")
    b: float = Field(description="This is the second number")


# ------------------ Tools ------------------
@tool(description="Add two numbers")
def add(a: int, b: int) -> int:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply,
    name="Multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)


# ------------------ LLM ------------------
llm = ChatOpenAI()

llm_with_tools = llm.bind_tools([add, multiply_tool])

# ------------------ Conversation ------------------
messages = [
    HumanMessage(content="What will be the answer when we add 20 and 20?")
]

# Step 1: Ask the LLM
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)


# ------------------ Execute Tool ------------------
tools = {
    "add": add,
    "Multiply": multiply_tool,
}

for tool_call in ai_message.tool_calls:
    selected_tool = tools[tool_call["name"]]

    tool_result = selected_tool.invoke(tool_call["args"])

    messages.append(
        ToolMessage(
            content=str(tool_result),
            tool_call_id=tool_call["id"],
        )
    )

# ------------------ Final Response ------------------
final_response = llm_with_tools.invoke(messages)

print("=" * 40)
print(final_response.content)
print("=" * 40)