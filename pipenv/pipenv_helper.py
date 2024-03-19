import os

print("\n---Running Python Pipenv Helper---\n")

print("Checking Python Version: ",end=" ")
os.system("cmd /c python --version") 

print("Checking Pip Version: ",end=" ")
os.system("cmd /c pip --version")

print("Showing all pip modules: ",end=" ")
os.system("cmd /c pip list")

print("Entering Pipenv virtual environment: ",end=" ")
os.system("cmd /c pipenv shell *")

print("Generate a list of all : ",end=" ")
os.system("cmd /c pip list")
