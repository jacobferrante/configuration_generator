import yaml

## Load YAML file into data dict
with open("questions/server.yaml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

## Save dicts. to variables to be used
prereqs = data["prereqs"]
questions = data ["questions"]

## Output filename based on user input or YAML file.
if prereqs["ask_filename"] == False:
    print("using default filename")
else:
    output_filename = input("What Filename would you like to use? ")

## Output folder based on user input or YAML file.
if prereqs["output_folder"] == None:
    output_folder = input("Where would you like to output this? ")
else:
    print("outputting file to " + prereqs["output_folder"])

## 
for k, v in questions.items():
    questions[k] = input(v)



