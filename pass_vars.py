#!/usr/bin/python

import sys, getopt

def main(argv):
	env_vars_string = ''
	template_dir = ''
	template_file = ''
	output_file = ''

	try:
		opts, args = getopt.getopt(argv,"he:d:f:o:",["env_vars_string=", "template_dir=", "template_file=", "output_file="])
	except getopt.GetoptError:
		print 'Example usage:' + '\n' + 'pass_vars.py -e <env_vars_string> -d <template_dir> -f <template_file> -o <output_file>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Example usage:' + '\n' + 'pass_vars.py -e <env_vars_string> -d <template_dir> -f <template_file> -o <output_file>'
			sys.exit()
		elif opt in ("-e", "--env_vars_string"):
			env_vars_string = arg
		elif opt in ("-d", "--template_dir"):
			template_dir = arg
		elif opt in ("-f", "--template_file"):
			template_file = arg
		elif opt in ("-o", "--output_file"):
			output_file = arg

	print 'env_vars_string:', env_vars_string
	print 'template_dir:', template_dir
	print 'template_file:', template_file
	print 'output_file:', output_file

if __name__ == "__main__":
	main(sys.argv[1:])