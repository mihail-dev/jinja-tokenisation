#!/usr/bin/env python

import os
from jinja2 import Template, Environment, FileSystemLoader

# Load environment variables
env_vars_string = "tomcat_generaloptions tomcat_debugjavaoptions standalone_javaoptions"
env_vars_list = env_vars_string.split()
env_vars_dict = {}

# Add environment variables to a dict
for env_var in env_vars_list:
	env_key = env_var
	env_value = os.environ[env_var]
	env_vars_dict[env_key] = env_value

# Load templates file
env = Environment(loader=FileSystemLoader('/opt/templates'))
template = env.get_template('local.properties.template')

# Tokenise
output_from_parsed_template = template.render(env_vars_dict)

print 'Tokenisation complete'

# save file
# TODO: append a file instead
with open('local.properties', "wb") as tokenised_file:
    tokenised_file.write(output_from_parsed_template)


