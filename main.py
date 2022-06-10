from genericpath import isdir
import yaml
import os

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"config.yaml")
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),"templates")
question_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "questions")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")

## load templates using jinja2
from jinja2 import FileSystemLoader, Environment
env = Environment (
    loader = FileSystemLoader(template_dir)
)

## Function to generate a printed list of files in a directory
def get_dir_list(dir_var, file_ext):
    ret = set()
    for root, dirs, files in os.walk(dir_var):
        for filename in files:
            ret.add(filename)
    return ret

def print_dict_formatted(directory, file_ext):
    for x in os.listdir(directory):
        print(x.replace(file_ext, ""))

while __name__ == "__main__":

    ## Print out list of templates, and have user choose a template and assign it to a variable to use
    question_choice = None
    while question_choice not in get_dir_list(question_dir, ".yaml"):
        print_dict_formatted(question_dir, ".yaml")
        question_choice = input("What data would you like to use? ") + '.yaml'
        yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), question_dir, question_choice)
        
    # Ask which template to use 
    user_template = None
    while user_template not in get_dir_list(template_dir, ".txt"):
        print_dict_formatted(template_dir, ".txt")
        user_template = input("what template(s) would you like to use? ")
        user_template = user_template + ".txt"
    ## Load YAML file into data dict
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    ## Save dicts. to variables to be used
    prereqs = data["prereqs"]
    questions = data ["questions"]

    ## assign values to dict item using user input 
    for k, v in questions.items():
        questions[k] = input(v)

    ## assign filename based on user input or yaml file
    if prereqs['ask_filename'] is True or prereqs['filename'] is None:
        output_filename = input("What would you like to name the file? ")
    else:
        print("Using predetermined filename")
        output_filename = prereqs["filename"]
    output_filename = output_filename + prereqs['file_extension']

    ## assign output locaton based on user input or yaml config
    if prereqs['output_location'] is None:
        output_location = input("Where would you like to export the completed file? ")
    else:
        print("Using predetermined output locaton")
        output_location = prereqs["output_location"]
    output_location = output_dir + "/" + output_location

    ## make the output directory if it does not exist
    if os.path.isdir(output_location) is False:
        os.mkdir(output_location)
    else:
        print("exporting to " + output_location)        
    
    ## create a variable that holds the final output path
    output_final = output_location + "/" + output_filename
    
    ## write file using user input and template/yaml.
    template = env.get_template(user_template)
    output = template.render(**questions)
    with open (output_final, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")
