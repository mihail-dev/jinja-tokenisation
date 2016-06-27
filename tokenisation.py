#!/usr/bin/env python

import os, sys, getopt
from jinja2 import Template, Environment, FileSystemLoader, meta

def main(argv):
	# Fetch options
	template_dir = ''
	template_file = ''
	output_file = ''

	try:
		opts, args = getopt.getopt(argv,"hd:f:o:",["template_dir=", "template_file=", "output_file="])
	except getopt.GetoptError:
		print 'Example usage:' + '\n' + 'tokenisation.py -d TEMPLATE_DIR -f TEMPLATE_FILE -o OUTPUT_FILE'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Example usage:' + '\n' + 'tokenisation.py -d TEMPLATE_DIR -f TEMPLATE_FILE -o OUTPUT_FILE'
			sys.exit()
		elif opt in ("-d", "--template_dir"):
			template_dir = arg
		elif opt in ("-f", "--template_file"):
			template_file = arg
		elif opt in ("-o", "--output_file"):
			output_file = arg

	# Load templates file
	env = Environment(loader=FileSystemLoader(template_dir))
	template = env.get_template(template_file)

	# Fetch and print all variables in tempalte file
	print 'Fetch and print all variables in template file'
	fetched_vars = []
	template_source = env.loader.get_source(env, template_file)[0]
	parsed_content = env.parse(template_source)
	fetched_vars = meta.find_undeclared_variables(parsed_content)
	print 'Fetched variables:', fetched_vars

	# Add environment variables to a dict
	env_vars_dict = {}
	for env_var in fetched_vars:
		env_key = env_var
		env_value = os.environ[env_var]
		env_vars_dict[env_key] = env_value

	# Tokenise
	output_from_parsed_template = template.render(env_vars_dict)

	print 'Tokenisation complete'

	# Save file
	with open(output_file, "wb") as tokenised_file:
	    tokenised_file.write(output_from_parsed_template)

if __name__ == "__main__":
	main(sys.argv[1:])