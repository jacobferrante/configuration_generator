import yaml
import os
import glob

def write_template(dict_name, template_file, template_type):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (template_file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")

def get_dir_list(file_ext):
    ret = set()
    for root, dirs, files in os.walk('questions'):
        for filename in files:
            ret.add(filename)
            if filename.endswith(file_ext):
                print(filename)
    return ret

## Print out file list in template directory, only ending in .yaml and ask user which file, ask again if file does not exist
file_choice = None
files = get_dir_list(".yaml")
yaml_dir = "questions"

while file_choice not in files:
    file_choice = input("What data would you like to use? ")
    yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), yaml_dir, file_choice)


## Load YAML file into data dict
with open(template_choice) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

## Save dicts. to variables to be used
prereqs = data["prereqs"]
questions = data ["questions"]

## Output filename based on user input or YAML file.
if prereqs["ask_filename"] == False:
    print("using default filename")
else:
    output_filename = input("What Filename would you like to use? ")

## Output folder based on user input or YAML file.s
if prereqs["output_folder"] == None:
    output_folder = input("Where would you like to output this? ")
else:
    print("outputting file to " + prereqs["output_folder"])

## assign values to dict item using user input 
for k, v in questions.items():
    questions[k] = input(v)
