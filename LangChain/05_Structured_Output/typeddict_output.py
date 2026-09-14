from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):

    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment:Annotated[Literal['pos','neg'], "Return sentiment of the review either negative, positive or netural"]
    pros: Annotated[Optional[list[str]],"Extract the pros which is discussed in this review"]
    cons: Annotated[Optional[list[str]], "Extract the cons discussed in this review"]
    name: Annotated[Optional[str],"Tell me the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
Analyze the following customer review.

Review:
 Radha Rani!                              
I ordered this gaming laptop after reading dozens of positive reviews. It arrived on time and the build quality is fantastic. Games run smoothly even on ultra settings, and the keyboard feels premium.

Unfortunately, after only two weeks the cooling fans started making loud noises. Customer support responded quickly and arranged a replacement, but the replacement unit had the same issue. The battery life is also disappointing, lasting barely three hours under normal use.

I really want to love this laptop because its performance is outstanding, but the quality control problems make it difficult to recommend without reservations.
""")

print(result['name'])