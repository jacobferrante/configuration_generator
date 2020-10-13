import yaml
import os
import glob
from jinja2 import FileSystemLoader, Environment
env = Environment (
    loader = FileSystemLoader('templates')
)

## Get the Jinja template and write to an output file
def write_template(dict_name, template_file, template_type):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (template_file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")
## Print off the file list in a directory
def get_dir_list(folder):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            print(os.path.splitext(filename)[0])
    
## Ask the user if they're manually inputting data and print the file list based off choice


config_type = None
while config_type not in("yes", "no"):
    config_type = input("Are you manually filling out data? (Yes, or No) ")
file_choice = None
if config_type == "yes":
    while file_choice not in("saewr", "asfsd"):
        get_dir_list("configurations")
        file_choice = input("What data would you like to use? ")
        yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configurations", file_choice + ".yaml")
elif config_type == "no":
    while file_choice not in():
        get_dir_list("precompiled")
        file_choice = input("What data would you like to use? ")
        yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "precompiled", file_choice + ".yaml") 




## open the user picked yaml file and load it
with open(yaml_file) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

## If user chooses manual input, it will ask for input to reassign dictionary values
if config_type == "yes":
    for k, v in data.items():
        v["answer"] = input(v["question"])
        data[k] = v
## Otherwise it will use the reference file and reassign the values
else:
    for k, v in data.items():
         data[k] = v

## write the output to a file
template_choice = input("what templates would you like to use? ")
template_final = template_choice.split()

file_ext = input("What is the file extension of your config? ")

for x in template_final:
    write_template(data, x + "." + file_ext, x + ".txt")




