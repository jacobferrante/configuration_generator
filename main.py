import yaml
import os
import glob



## Write dictionary to template/file
def write_template(dict_name, template_file, template_type):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (template_file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")

## Function to generate a printed list of files in a directory
def get_dir_list(file_ext):
    ret = set()
    for root, dirs, files in os.walk('questions'):
        for filename in files:
            ret.add(filename)
            if filename.endswith(file_ext):
                print(filename)
    return ret

if __name__ == "__main__":
    from jinja2 import FileSystemLoader, Environment
    env = Environment (
        loader = FileSystemLoader('questions/templates')
    )
    ## Print out file list in template directory, only ending in .yaml and ask user which file, ask again if file does not exist
    file_choice = None
    files = get_dir_list(".yaml")
    yaml_dir = "questions"
    
    ## Print out list of templates, and have user choose a template and assign it to a variable to use
    while file_choice not in files:
        file_choice = input("What data would you like to use? ")
        yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), yaml_dir, file_choice)

    ## Load YAML file into data dict
    with open(yaml_file) as f:
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
        output_folder = prereqs["output_folder"]

    ## assign values to dict item using user input 
    for k, v in questions.items():
        questions[k] = input(v)

    ## Check if output directory exists and create it if it doesn't
    if os.path.isdir(output_folder) == False:
        os.mkdir("outputs/" + output_folder)
    else:
        print("folder exists")

    
    # Ask which template to use 
    template_choice = input("what templates would you like to use? ")
    template_final = template_choice.split()
    

    ## 
    for x in template_final:
        outputs = os.path.join(os.path.dirname(os.path.abspath(__file__)), output_folder, x)
        write_template(questions, outputs, x)