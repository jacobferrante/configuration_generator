# configmaker
config maker using python, jinja2 and yaml.


It uses the yaml files for the questions to be asked and the txt files to be used as jinja2 templates.

So far, the folders you need to have is "configurations" and "templates"

When you run the script, it will ask which file you'd like to build, it will search the configurations folder for your choices to use.
You must have a matching template to your yaml file, such as setup.yaml and setup.txt.