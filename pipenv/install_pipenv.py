import os

print("\n---Running Python Pipenv Installer---\n")

print("Installing Pipenv: ",end=" ")
os.system("cmd /c pip install --user pipenv") 

print("Show current directory: ",end=" ")
os.system("echo %cd%") 

print("Entering virtual shell: ",end=" ")
os.system("pipenv shell")

os.system("") 

print("show me cmd.. pip list")
os.system("pip list")

print("Installing the popular 'requests' python package on the virtual enviornment: ",end=" ")
os.system("cmd /c pipenv install requests")

# print("Displaying all pip packages on virutal env: ",end=" ")
# os.system("cmd /c pip list")

# print("Exiting out of virtual shell: ",end=" ")
# os.system("cmd /c exit exit")

# print("Displaying all pip packages on local env: ",end=" ")
# os.system("cmd /c pip list")
