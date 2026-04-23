from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import tools

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools: list[str]

llm = ChatOpenRouter(model="meta-llama/llama-3.3-70b-instruct")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = f"""
You are a research assistant that will generate a detailed research paper. Answer the user query and use necessary tools.
Make sure the summary is a detailed paragraph of at least 5-6 sentences covering the topic thoroughly.
Include key facts, history, scientific significance, and current research in the summary.
Wrap the output in this format and provide no other text.
{parser.get_format_instructions()}
"""

# create_agent uses system_prompt as a string

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt,
    response_format=ResearchResponse,  
)

query = input("What do you want to research about?")

raw_response = agent.invoke({
    "messages": [("human", f"Research about: {query}. Then save the output to a file.")]
})

# try and catch is model causes some error while giving the output
try:
    structured_response = raw_response.get("structured_response")
    print(structured_response)
except Exception as e :
    print("Error parsing response" , e , "raw_response - " , raw_response)


# TOOLS - Tools are things that LLM/Agents can use, that we can write ourselves or can bring in from langchain community hub
