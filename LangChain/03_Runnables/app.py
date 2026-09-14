from dummy_prompt import DummyPromptTemplate
from dummy_llms import DummyLlm
from dummy_chain import Chain

template = DummyPromptTemplate(

    template="""
You are a helpful assistant.

Generate a joke about {topic}
in {language}.
""",

    input_variables=[
        "topic",
        "language"
    ]
)

llm = DummyLlm()

chain = Chain(
    llm,
    template
)

response = chain.run({

    "topic":"teacher",

    "language":"Hindi"

})

print(response)