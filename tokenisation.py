#!/usr/bin/env python

import os
from jinja2 import Template, Environment, FileSystemLoader
import sys, getopt

def main(argv):
	# Fetch options
	env_vars_string = ''
	template_dir = ''
	template_file = ''
	output_file = ''

	try:
		opts, args = getopt.getopt(argv,"he:d:f:o:",["env_vars_string=", "template_dir=", "template_file=", "output_file="])
	except getopt.GetoptError:
		print 'Example usage:' + '\n' + 'tokenisation.py -e ENV_VARS_STRING -d TEMPLATE_DIR -f TEMPLATE_FILE -o OUTPUT_FILE'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Example usage:' + '\n' + 'tokenisation.py -e ENV_VARS_STRING -d TEMPLATE_DIR -f TEMPLATE_FILE -o OUTPUT_FILE'
			sys.exit()
		elif opt in ("-e", "--env_vars_string"):
			env_vars_string = arg
		elif opt in ("-d", "--template_dir"):
			template_dir = arg
		elif opt in ("-f", "--template_file"):
			template_file = arg
		elif opt in ("-o", "--output_file"):
			output_file = arg

	# Load environment variables
	env_vars_list = env_vars_string.split()
	env_vars_dict = {}

	# Add environment variables to a dict
	for env_var in env_vars_list:
		env_key = env_var
		env_value = os.environ[env_var]
		env_vars_dict[env_key] = env_value

	# Load templates file
	env = Environment(loader=FileSystemLoader(template_dir))
	template = env.get_template(template_file)

	# Tokenise
	output_from_parsed_template = template.render(env_vars_dict)

	print 'Tokenisation complete'

	# Save file
	# TODO: append a file instead
	with open(output_file, "wb") as tokenised_file:
	    tokenised_file.write(output_from_parsed_template)

if __name__ == "__main__":
	main(sys.argv[1:])