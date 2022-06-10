# Configuration Generator

A configuration file creator using Python, PyYaml, and Jinja2. Used to quickly create configuration files from templates and user input.

You will need to install jinja2 and pyyaml manually. 
```bash
pip install jinja2
```

```bash
pip install pyyaml
```

## Building Configuration Files

The YAML file contains the questions that needed to be asked to fill in the Jinja2 Template. You will be asked which YAML file to use.

I have added a prereqs section which allows you to predefine settings based on each .yaml file, so far I've added the ability to manual enter a file name, or use one that matches the template name. A option to set the file extension for the completed file, and the output folder location, which leave blank if want to specify during file creation.

Here is an example of the prereqs which would use the template name as the filename, use the file extension .ini and output to the folder "outputs"

```yaml
prereqs: 
        filename: "server123" # Set predetermined filename 
        file_extension: ".txt" # Set predetermined extension, leave blank if you want none 
        ask_filename: False # If you'd like the script to ask you for a custom filename, make this True
        output_location: test # leave blank if prefer to choose during file creation
```
These values would ask for an IP address and then assign them to the value. IP 

```yaml
questions:
        # variable to reference in template : "question to ask in script"
        ip_address1: "What is the first IP? "
        ip_address2: "What is the second IP? "
        ip_address3: "What is the third IP? "
        ip_address4: "What is the fourth IP? "
```

After you've filled in your data through user input, it will ask for a template(s), this is an example on how to format your templates.
```bash
ip_address1: {{ ip_address1 }}
ip_address2: {{ ip_address2 }}
```

