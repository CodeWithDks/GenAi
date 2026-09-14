from pydantic import BaseModel, Field
from langchain_core.tools import StructuredTool


class MultiplyInput(BaseModel):
    a: int = Field(description="The first number to multiply")
    b: int = Field(description="The second number to multiply")


def multiply_func(a: int, b: int) -> int:
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name='multiply',
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)

result = multiply_tool.invoke({"a": 2, "b": 11})
print(result)