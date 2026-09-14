from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
#from using_pydatic_tool import MultiplyInput


class MultiplyInput(BaseModel):
    a : int = Field(description='This is the first number')
    b : int = Field(description='This is the second number')


class MultiplyTool(BaseTool):
    name : str = 'multiply'
    description : str = 'multiply two number'

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a : int, b : int) -> int:
        return a * b
    
multiply_tool = MultiplyTool()

result = multiply_tool.invoke({'a':2, 'b':10})

print(result)
         
