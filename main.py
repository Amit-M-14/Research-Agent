# from dotenv import load_dotenv
# from langchain_classic.agents import AgentExecutor
# from pydantic import BaseModel
# from langchain_openrouter import ChatOpenRouter
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import PydanticOutputParser
# from langchain.agents import create_agent


# load_dotenv()

# class ResearchResponse(BaseModel):
#     topic : str
#     summary : str
#     sources : list[str]
#     tools : list[str]

# llm = ChatOpenRouter(model="meta-llama/llama-3.1-8b-instruct")

# # response = llm.invoke("What is the meaning of life?")
# # print(response)

# # Prompt template 
# parser = PydanticOutputParser(pydantic_object=ResearchResponse)
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
#             You are a research assistant that will generate a research paper.Answer the user query and use necessary tools.
#             wrap the output in this format and provide no other text. \n{format_instructions}
#             """,
#         ),
#         ("placeholder","{message}"),
#         ("human","{query}"),
#         ("placeholder","{agent_scratchpad}"),
#     ]
# ).partial(format_instructions=parser.get_format_instructions())

# # creating the agent

# agent = create_agent(
#     model = llm,
#     # prompt = parser.get_format_instructions(),
#     tools = []
# )
# agent_executor = AgentExecutor(agent=agent,tools=[],verbose=True)
# raw_response = agent_executor.invoke({"query":"What is a Blackhole"})
# print(raw_response)

from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools: list[str]

llm = ChatOpenRouter(model="openai/gpt-4o-mini")

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

system_prompt = f"""
You are a research assistant that will generate a research paper. Answer the user query and use necessary tools.
Wrap the output in this format and provide no other text.
{parser.get_format_instructions()}
"""

# ✅ create_agent uses system_prompt as a string, no ChatPromptTemplate needed
agent = create_agent(
    model=llm,
    tools=[],
    system_prompt=system_prompt,
    response_format=ResearchResponse,  # ✅ structured output directly
)

raw_response = agent.invoke({
    "messages": [("human", "What is a Blackhole")]
})

print(raw_response)