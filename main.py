import yaml
import jinja2
import os
import glob


## List the files within the YAML directory for user choice ###
for root, dirs, files in os.walk("yaml"):
    for filename in files:
        print(os.path.splitext(filename)[0])

### Let the user choose the file to build and append .yaml to choice ###
file_choice = input("What would you like to build a config for today? ")
file_choice = file_choice + ".yaml"

### load in the user choice file for the YAML and jinja2 template ###
txt_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/templates", file_choice )
yaml_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/yaml", file_choice)

questions = glob.glob(yaml_files)
templates = glob.glob(txt_files)

with open(questions) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

print(data)