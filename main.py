from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openrouter import ChatOpenRouter

load_dotenv()

llm = ChatOpenRouter(model="meta-llama/llama-3.1-8b-instruct")

response = llm.invoke("What is the meaning of life?")
print(response)