#!/usr/bin/python3

from core import Core
from datetime import datetime
import os,sys

root_path = os.path.dirname(os.path.abspath(__file__)) + "/../"
rule_path = root_path + "/resource/rules.json"

folder_path = ""
output_path = ""

def control():
    if (len(sys.argv) != 2):
        help()
        sys.exit()
    else:
        global folder_path
        folder_path = sys.argv[1]

        global output_path
        output_path = folder_path + str(datetime.today()).replace(" ","-") + "-result.json"


def help():
    print ("[!] There is an error while giving arguments")
    print ("python main.py /Users/tom/Desktop/Test/")

if __name__ == '__main__':
    control()
    c = Core(folder_path,rule_path,output_path)
    files = c.allFilesinFolder()
    rules = c.readRulesFromJson()
    
    print ("Seek4Treasure is started")
    
    #Walk in all files
    for file in files:
        c.readFile(file)    

    #After everything finish create result
    c.create_output()

    print ("Everything is okay. Result path is " + output_path)
    