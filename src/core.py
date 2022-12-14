from helper import Helper
from os import walk
import json,re,sys

class Core:
    """
    Class
    """

    def __init__(self, folder_path, rule_file, output_path):
        self.files = []
        self.rules = []
        self.pre_result = []
        self.folder_path = folder_path
        self.rule_file = rule_file
        self.output_path = output_path

        self.start()

       
    def start(self):
        """
        """
        print ("Seek4Treasure is started ")

        self.allFilesinFolder()
        self.readRulesFromJson()

        for file in self.files:
            self.readFile(file)
        
        self.create_output()


    def readRulesFromJson(self):
        """
        """
        try:
            input_file = open(self.rule_file, encoding="utf8", errors='ignore')
            json_array = json.load(input_file)
        except Exception:
            print("There is an error while reading rules.json file. Please control it")
            sys.exit()

        for item in json_array:
            store_details = {"key": None, "value": None}
            store_details['key'] = item['key']
            store_details['value'] = item['value']
            self.rules.append(store_details)

    def allFilesinFolder(self):
        """
        """
        for (dir_path, dir_names, files_name) in walk(self.folder_path):
            for file_name in files_name:

                self.files.append(Helper.last_char_control(dir_path,"/") + file_name)

    def readFile(self, filename):
        """
        """
        try:
            with open(filename, "r", encoding="utf8", errors='ignore') as file:
                count = 0
                tmp_line_list = []
                lines = file.readlines()

            # read file and remove \n or space
            for line in lines:
                count += 1
                if line.rstrip() != "":
                    tmp_line_list.append([line.rstrip(),count])

            for line in tmp_line_list:
                rule = self.ruleControl(line[0])
                if rule is not None:
                    self.result(filename, rule, line[0],line[1])
        except:
            print ("There is an error while reading " + filename + " named file")
            sys.exit()

   
    def ruleControl(self, line):
        """
        """
        for rule in self.rules:
            result = re.search(rule["value"], line)
            if result:
                return rule["key"]


    def result(self, filename, rule, line, number):
        """
        """
        self.pre_result.append(
            {"filename": filename, "rule": rule, "line": line, "number":number})

 
    def create_output(self):
        """
        Erdemstar
        """
        if self.pre_result != []:
            try:
                with open(self.output_path, 'w') as f:
                    f.write(json.dumps(self.pre_result))
                    print ("Check file content for potential secrets")
                    print ("Result path is " + self.output_path)
            except:
                print ("There is an error while creating result file")

            Helper.close_type(1)
        else:
            print ("It looks everyting is okay. Go for commit")
            Helper.close_type(0)

    

