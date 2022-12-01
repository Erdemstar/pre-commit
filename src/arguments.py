from helper import Helper
import argparse

class Argument:
    def __init__(self):
        self.my_parser = ""
        self.args = ""

    def helper(self):
        self.my_parser = argparse.ArgumentParser(
            prog="seek4treasure.py", usage='%(prog)s  --folder_path /home/user/code/ --output_path /home/user/code/ --rule_file /home/user/seek4treasure/resource/rule.json', description="This is helper of seek4treasure")
        self.my_parser.add_argument('--folder_path', type=str, required=True,
                                    help="This is code base path which will be control by seek4treasure")
        self.my_parser.add_argument(
            '--output_path', type=str, required=True, help="This is output path")
        self.my_parser.add_argument(
            '--rule_file', type=str, required=True, help="This is rule file path")
        self.args = self.my_parser.parse_args()

        if self.args.folder_path == "./" or self.args.output_path == "./":
            self.args.folder_path = Helper.get_current_path()
            self.args.output_path = Helper.get_current_path()

        return {"folder_path": self.args.folder_path, "output_path": self.args.output_path, "rule_file": self.args.rule_file}
