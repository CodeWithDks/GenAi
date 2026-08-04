from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field
from typing import Type


# -----------------------------
# Input schema for Subtract tool
# -----------------------------
class SubtractInput(BaseModel):
    a: int = Field(description="This is the first number")
    b: int = Field(description="This is the second number")


# -----------------------------
# Input schema for Divide tool
# -----------------------------
class DivideInput(BaseModel):
    a: int = Field(description="This is the first number")
    b: int = Field(description="This is the second number")


# ==========================================================
# 1. @tool
# ==========================================================
# The easiest way to create a LangChain tool.
# Best for simple functions where LangChain can automatically
# infer the input parameters and return type.
@tool(description="Add two numbers")
def add(a: int, b: int) -> int:
    return a + b


# Normal Python function
def subtract(a: int, b: int) -> int:
    return a - b


# ==========================================================
# 2. StructuredTool
# ==========================================================
# Used when you want to explicitly define the input schema
# using a Pydantic model.
#
# Advantages:
# - Better validation
# - Better parameter descriptions
# - More control over tool inputs
subtract_tool = StructuredTool.from_function(
    func=subtract,
    name="Subtract",
    description="Subtract two numbers",
    args_schema=SubtractInput
)


# ==========================================================
# Another simple @tool example
# ==========================================================
@tool(description="Multiply two numbers")
def multiply(a: int, b: int) -> int:
    return a * b


# ==========================================================
# 3. BaseTool
# ==========================================================
# Used for advanced/custom tools.
#
# Choose BaseTool when:
# - You need custom execution logic
# - You want error handling
# - You need API calls
# - You need database access
# - You want to maintain internal state
#
# It requires implementing the _run() method.
class Divide(BaseTool):

    # Tool name shown to the LLM
    name: str = "Divide"

    # Description helps the LLM decide when to use the tool
    description: str = "Divide two numbers"

    # Input schema
    args_schema: Type[BaseModel] = DivideInput

    # Logic executed when the tool is called
    def _run(self, a: int, b: int) -> float:

        # Handle invalid input
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b


# Create an instance of the custom tool
divide_tool = Divide()


# ==========================================================
# Toolkit
# ==========================================================
# A toolkit is simply a collection of related tools.
# It makes it easy to pass multiple tools to an agent.
class MathToolkit:

    def get_tools(self):
        return [
            add,
            subtract_tool,
            multiply,
            divide_tool
        ]


# Create toolkit object
toolkit = MathToolkit()

# Get all tools
tools = toolkit.get_tools()


# Print tool information
for tool in tools:
    print(tool.name, "=", tool.description)


# Let's test each tools
print('----------Addition-----------------')
print(add.invoke({"a": 10, "b": 5}))


print('----------Subtraction-----------------')
print(subtract_tool.invoke({'a':21, 'b':11}))

print('----------Multiplication-----------------')
print(multiply.invoke({'a':12, 'b':5}))

print('----------Addition-----------------')
print(divide_tool.invoke({'a':12, 'b':3}))