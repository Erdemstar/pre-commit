# Pre-commit
I developed an application by examining the pre-commit structure available in this repository Git Hooks and using it. For a better understanding of the project, I wrote the parts used in the project structure below.

## Project Components

**Pre-commit**  : Git hooks are scripts that run automatically every time a particular event occurs in a Git repository. The pre-commit script is executed every time you run git commit before Git asks the developer for a commit message or generates a commit object.

**seek4treasure**: The given Rules.json parses and reads the rules and checks whether they exist in the target project. If the entered rules match a file in the project, it prevents the progress of the commit process by sending sys.exit(0) and produces a result file showing which rule is in which file and line by producing a result file. Otherwise, the commit process takes place.

## Setup
In order to activate the pre-commit in the relevant project and to search with Rules.json and get the result, the following must be applied beforehand.

### Pre-commit definition
Copy the downloaded <file-path>/pre-commit/resource/pre-commit.sample file as pre-commit into <file-path>/project/.git/hooks/ in your project.

```
cp <file-path>/pre-commit/resource/pre-commit.sample <file-path>/project/.git/hooks/pre-commit
```

After the copying process, the executable right must be given for the pre-commit script to run.

```
chmod +x <file-path>/project/.git/hooks/pre-commit.sh
```

Similar operation should be done in seek4treasure.

```
chmod +x  <file-path>/pre-commit/src/seek4treasure.py
```

### Installing dependencies
In order for the seek4treasure project to work in pre-commit, dependencies must be installed with pip3.

```
pip3 install -r <file-path>/pre-commit/requirements.txt
```

### Environment variable editing
In this step, the user Environment variable must be added to the project path so that seek4treasure.py can run from any location on the machine. Below is an example for .bashrc

```
echo "export PATH="<file-path>/pre-commit/src:$PATH" >> .bashrc
```

### Control
After the above steps, you need to run the following command and get the help output.

```
seek4treasure.py -h  

usage: seek4treasure.py  --folder_path /home/user/code/ --output_path /home/user/code/ --rule_file /home/user/seek4treasure/resource/rule.json

This is helper of seek4treasure

  -h, --help            show this help message and exit
  --folder_path FOLDER_PATH
                        This is code base path which will be control by seek4treasure
  --output_path OUTPUT_PATH
                        This is output path
  --rule_file RULE_FILE
                        This is rule file path
```
