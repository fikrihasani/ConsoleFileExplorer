from pathlib import Path
import os
import json

commands = ["index","help"]

# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def check(p):
    if str(p).split("/")[-2] == "":
        return "/" 
    else:
        return str(p).split("/")[-2]

def indexing():
    dat = {}
    # basePath = os.path.abspath('.').split(os.path.sep)[0]+os.path.sep
    basePath = "/home/fikri"
    # print(basePath)
    i = 1
    for p in Path(basePath).rglob( '*' ):
        dir_name = str(p).split("/")[-1]
        if dir_name not in dat.keys():
            dat[dir_name] = [
                {
                    "path": str(p),
                    "dir": os.path.isdir(p),
                    "file": os.path.isfile(p),
                    "parent": check(p)
                }
            ]
        else:
            dat[dir_name].append(
                {
                    "path": str(p),
                    "dir": os.path.isdir(p),
                    "file": os.path.isfile(p),
                    "parent": check(p)
                }
            )
        
        print(f"Folder atau file ke {i}")
        print([str(p),str(p).split("/")[-1],os.path.isdir(p),os.path.isfile(p)])
        i+=1
        sleep(0.05)
        clear()
        
    with open("fileIndex.json", "w") as outfile:
        json.dump(dat, outfile)

def list_of_command():
    print("current supported commands: ")
    print("1. Index")

def help():
    print("command can be inputted with format as follows: ")
    print("<command> [<filename> [<destination]]")
    list_of_command()

if __name__ == "__main__":
    inp = input().split()
    if(len(inp) == 1):
        if inp == "index":
            indexing()
        elif inp == "help":
            help()
        else:
            list_of_command()

