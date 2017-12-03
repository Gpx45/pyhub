import sys
import os

system = sys.platform
print(system)
# We provide the name of current OS system you are running here.
version = sys.version

# print('\n',version, '\n')

# prints out the current version of Python you are running.
# mind you before hand we placed a newline escape sequence.

cwd = os.getcwd()
# print(cwd,'\n')

# Prints current working directory that you are in.
env = os.environ
# print(env)

# In this case you can call a attribute instantly
# or
# call the function that uses that attribute for a specific purpose.

getHome = os.getenv('Home')
print('\n', getHome)
