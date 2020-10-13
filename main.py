import yaml
import os
import glob

## Get the Jinja template and write to an output file
def write_template(dict_name, template_file, template_type):
    template = env.get_template(template_type)
    output = template.render(**dict_name)
    with open (template_file, 'w') as f:
        f.write(output)
    print("Your configuration file is complete!")

## list the files in a directory and save them to a list
def get_dir_list(folder, file_ext):
    ret = set()
    for root, dirs, files in os.walk(folder):
        for filename in files:
            ret.add(filename)
            if not filename.endswith(file_ext):
                print(filename)
    return ret
    
if __name__ == "__main__":
    ### Ask the User which configuration mode they want to use, manual entry or precompiled data ###
    config_mode = None
    while config_mode not in("YES", "NO"):
        config_mode = input("Are you manually filling out data? (Yes, or No) ").upper()
    file_choice = None
    if config_mode == "YES":
        files = get_dir_list("questions", ".txt")
        yaml_dir = "questions"
    elif config_mode == "NO":
        files = get_dir_list("precompiled", ".txt")
        yaml_dir = "precompiled"
    while file_choice not in files:
        file_choice = input("What data would you like to use? ")
    yaml_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), yaml_dir, file_choice)
    ### Load the templates based on Config Mode  ###
    from jinja2 import FileSystemLoader, Environment
    env = Environment (
        loader = FileSystemLoader(yaml_dir + '/templates')
    )
    ### Load the YAML file based on user input ###
    with open(yaml_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    ### Load the correct value reassignment method based on user input ###
    if config_mode == "YES":
        for k, v in data.items():
            v["answer"] = input(v["question"])
            data[k] = v
    else:
        for k, v in data.items():
            data[k] = v
    ### Pick and load template(s) based on user input ###
    get_dir_list(yaml_dir, ".yaml")
    template_choice = input("what templates would you like to use? ")
    template_final = template_choice.split()

    ### Write the data to the templates ###
    for x in template_final:
        outputs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs", x)
        write_template(data, outputs, x)


        ## TO DO ##
        # Need to add Error checking on the template user input while keeping the ability to use multiple templates at once




