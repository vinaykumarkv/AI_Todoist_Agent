from dotenv import load_dotenv

load_dotenv()
import os

from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_core.core_schema import model_field
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor

from todoist_api_python.api import TodoistAPI

todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEM_API_KEY")
todoist = TodoistAPI(todoist_api_key)


@tool
def add_task(task, description):
    """Add a new tasks to the users task list"""
    todoist.add_task(content=task,
                     description=description)
@tool
def show_task():
    """Show all tasks list from todo list when user wants to see all the tasks"""
    res = todoist.get_tasks()
    print(res)
    tasks = []
    for task in res:
        for t in task:
            tasks.append(t.content)
    return tasks

tools = [add_task, show_task]

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = ("""You are a helpful assistant, 
                 You will help the user add tasks. 
                 If the user asks to show the tasks: for example, "show me the tasks", 
                 then print all the tasks to user in bullet list.
                 """)

prompt = ChatPromptTemplate([
    ("system", system_prompt),
    MessagesPlaceholder("history"),  # Move history before input for better flow
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

# Initialize history BEFORE first use
history = []

# Main conversation loop
while True:
    user_input = input("You: ")

    # Invoke with history included
    response = agent_executor.invoke({"input": user_input, "history": history})

    print(response['output'])

    # Update history after each interaction
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response['output']))