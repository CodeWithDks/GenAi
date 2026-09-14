from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.output_parsers import StrOutputParser

search = DuckDuckGoSearchResults()
parser = StrOutputParser()
result = search.invoke('Today top 5 it news')
output = parser.invoke(result)

print(output)