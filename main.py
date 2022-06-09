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

if __name__ == "__main__":

    ## Print out list of templates, and have user choose a template and assign it to a variable to use
    question_choice = None
    while question_choice not in get_dir_list(question_dir, ".yaml"):
        print(os.listdir(question_dir))
        question_choice = input("What data would you like to use? ")
        yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), question_dir, question_choice)

    # Ask which template to use 
    user_template = None
    while user_template not in get_dir_list(template_dir, ".txt"):
        print(os.listdir(template_dir))
        user_template = input("what template(s) would you like to use? ")

    ## Load YAML file into data dict
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    ## Save dicts. to variables to be used
    prereqs = data["prereqs"]
    questions = data ["questions"]

    ## assign values to dict item using user input 
    for k, v in questions.items():
        questions[k] = input(v)

    ## write file using user input and template/yaml
    template = env.get_template(user_template)
    output = template.render(**questions)
    with open ("outputs/file", 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")
