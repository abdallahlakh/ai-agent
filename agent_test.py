from agent_action import run_agent
from agent_tool import run_command
response = run_agent("can you create to me a file with the name hamdullah in this directory you don't need to create other directory?")
print(response['output'])
final=run_command(response['output'])