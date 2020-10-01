import yaml
import os
import glob
from jinja2 import FileSystemLoader, Environment
env = Environment (
    loader = FileSystemLoader('templates')
)

## Get the Jinja template and write to an output file
def write_template(template_type, dict_name, file):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")  

# List the files within the YAML directory for user choice ###
for root, dirs, files in os.walk("yaml"):
    for filename in files:
        print(os.path.splitext(filename)[0])

## Let the user choose the file to build and append .yaml to choice ###
file_choice = input("What would you like to build a config for today? ")

## load in the user choice file for the YAML and jinja2 template ###
txt_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/templates", file_choice )
yaml_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/yaml", file_choice)

questions = glob.glob(yaml_files)
templates = glob.glob(txt_files)

with open("yaml/questions.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

for k, v in data.items():
    v["answer"] = input(v["question"])
    #  you may or may not need this next line
    data[k] = v

print(data)

write_template(file_choice + ".txt", data, "output.ini")