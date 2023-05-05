from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback

load_dotenv()
agent = create_csv_agent(OpenAI(temperature=0), 'data.csv', verbose=True)

with get_openai_callback() as cb:
  print(agent.run("How many rows are there?"))
  print(cb)