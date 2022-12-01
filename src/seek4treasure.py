#!/usr/bin/python3

from core import Core
from helper import Helper
from arguments import Argument
from datetime import datetime
import sys
    

if __name__ == '__main__':
    a = Argument()
    params = a.helper()
    if params is not None:
        folder_path = Helper.last_char_control(params["folder_path"],"/")
        rule_file = params["rule_file"]
        output_path = Helper.last_char_control(params["output_path"],"/") + str(datetime.now()).replace(" ","_") + "_seek4treasure-result.json"

        c = Core(folder_path,rule_file,output_path)
        
    else:
        print ("There is an error while giving parametrers")
        sys.exit()
    
    
