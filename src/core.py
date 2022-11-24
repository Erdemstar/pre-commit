from os import walk
import json
import re


class Core:

    #
    #
    #
    def __init__(self, folder_path, rule_path, output_path):
        self.files = []
        self.rules = []
        self.pre_result = []
        self.folder_path = folder_path
        self.rule_path = rule_path
        self.output_path = output_path

    #
    #
    #
    def readRulesFromJson(self):
        input_file = open(self.rule_path, encoding="utf8", errors='ignore')
        json_array = json.load(input_file)

        for item in json_array:
            store_details = {"key": None, "value": None}
            store_details['key'] = item['key']
            store_details['value'] = item['value']
            self.rules.append(store_details)
        return self.rules

    #
    #
    #
    def allFilesinFolder(self):
        for (dir_path, dir_names, files_name) in walk(self.folder_path):
            for file_name in files_name:
                self.files.append(str(dir_path + file_name))
        return self.files

    #
    #
    #
    def readFile(self, filename):
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

    #
    #
    #
    def ruleControl(self, line):
        for rule in self.rules:
            result = re.search(rule["value"], line)
            if result:
                return rule["key"]

    #
    #
    #
    def result(self, filename, rule, line, number):
        self.pre_result.append(
            {"filename": filename, "rule": rule, "line": line, "number":number})

    #
    #
    #
    def create_output(self):
        with open(self.output_path, 'w') as f:
            f.write(json.dumps(self.pre_result))