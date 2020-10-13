# Config Maker

A configuration file creator using Python, PyYaml, Jinja2 and JSON. Used to quickly create configuration files from templates and user input and or compiled data. 

You will need to install jinja2 and pyyaml manually, JSON is native to Python.
```bash
pip install jinja2
```

```bash
pip install pyyaml
```


## Overview

You can generate configuration files in two different ways. Manually entering data, or using a precompiled set of data.
The templates and YAML files change depending on if you're entering manually or using precompiled data.

You will be asked if you want to enter data manually or not, either way you'll be asked which YAML data to load and which template(s) you want to export too.

When choosing a YAML file, just enter the name of the file.

When asked for a template, you can enter in multiple, just use a space in-between

## Manually Entering Data

The YAML file contains the questions that needed to be asked to fill in the Jinja2 Template. You will be asked which YAML file to use.
```yaml
ip_address1: 
        question: "What is the first IP? "
ip_address2:
        question: "What is the second IP? "
```

After you've filled in your data through user input, it will ask for a template(s), this is an example on how to format your templates.
```bash
ip_address1: {{ ip_address1.answer }}
ip_address2: {{ ip_address2.answer }}
```
## Precompiled Data

You can set up a YAML file to work as a dictionary of presaved items to push out to multiple templates at a time. 
```yaml
cylinder_count: 
        "v8"
wheel_size:
        "20 inch"
horsepower: 
        "276hp"
seats:
        "4"
```

The templates are slightly different from the manual entry ones, you do not need to add ".answer" at the end of your item.
You can also call to multiple templates easily by just entering multiple templates when asked.

car_spec.txt
```bash
This car has a {{ cylinder_count }} engine
and {{ wheel_size }} wheels, 
```

car_spec2.txt
```bash
along with {{ horsepower }} at the {{ wheel_size }} wheels. And it will seat {{ seats }} comfortably.
```
