from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages 
from langchain_google_genai import ChatGoogleGenerativeAI 
import os 
from dotenv import load_dotenv 
from langgraph.prebuilt import ToolNode, tools_condition 
from langgraph.graph import StateGraph, START, END 
from langchain_core.tools import tool 
from langchain.schema import SystemMessage 
import subprocess

load_dotenv() 

class State(TypedDict): 
    messages: Annotated[list, add_messages] 
    
@tool 
def run_command(cmd: str): 
    """Takes a command line prompt and executes it on the user's machine and returns the output of the command. My machine is window, so run window command. Always run command in my current working directory, if path is not specified. Example: run_command(cmd="dir") where ls is the command to list the files. """ 
    try:
        completed_process = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        return completed_process.stdout if completed_process.returncode == 0 else completed_process.stderr
    except Exception as e:
        return str(e) 

llm = ChatGoogleGenerativeAI( 
    model="gemini-2.5-flash", 
    api_key=os.getenv("GOOGLE_API_KEY"), )

llm_with_tool = llm.bind_tools(tools=[run_command]) 

def chatbot(state: State): 
    system_prompt = SystemMessage(content=""" You are an AI Coding assistant who takes an input from user and based on available tools you choose the correct tool and execute the commands. You can even execute commands and help user with the output of the command. Always make sure to keep your generated files in chat_gpt/ folder. """) 
    
    message = llm_with_tool.invoke([system_prompt] + state["messages"]) 
    assert len(message.tool_calls) <= 1 
    return {"messages": [message]} 

tool_node = ToolNode(tools=[run_command])
graph_builder = StateGraph(State) 
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges(
    "chatbot", 
    tools_condition )
graph_builder.add_edge("tools", "chatbot") 
graph_builder.add_edge("chatbot", END) 

# graph without memory 
graph = graph_builder.compile() 

# new graph with checkpointer 
def create_chat_graph(checkpointer): 
    return graph_builder.compile(checkpointer=checkpointer)