import yaml
import os
import glob
from jinja2 import FileSystemLoader, Environment
env = Environment (
    loader = FileSystemLoader('templates')
)

## Get the Jinja template and write to an output file
def write_template(template_type, dict_name, template_file):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (template_file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")  

# List the files within the YAML directory for user choice ###
for root, dirs, files in os.walk("configurations"):
    for filename in files:
        print(os.path.splitext(filename)[0])
        
## Let the user choose the file to build and append .yaml to choice ###

file_choice = input("What would you like to build a config for today? ")

## load in the user choice file for the YAML ###
yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configurations", file_choice + ".yaml")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")

## open the user picked yaml file and load it
with open(yaml_file) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


# assign new values to the dictionary based on user input

file_creation = input("Are you manually entering data? ")

if file_creation == "yes":
    for k, v in data.items():
        v["answer"] = input(v["question"])
        data[k] = v
else:
    for k, v in data.items():
         data[k] = v


## write the output to a file
write_template(file_choice + ".txt", data, file_choice)