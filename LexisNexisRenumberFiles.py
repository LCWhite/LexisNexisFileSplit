#! /usr/bin/env python3
# LexisNexisRenameFiles.py - Takes LexisNexis files that are mis-numbered
# after splitting with the LexisNexisFunctionsSplot.py script and adjusts the
# numbers

import shutil, os, re, send2trash

# Create a new folder to store the renamed files
os.makedirs('ReNumbered')

start_number = input("Enter the number by which you want the number tag to increase (e.g. 1, 500): ")
start_number = int(start_number)

# Create a regex that recognizes the file names
lxnxfilePattern = re.compile(r"""^(.*?)			# some base name text
							(\d+)				# the file number
							(\.txt)
							""", re.VERBOSE)

# Loop over the LexisNexis files
for old_file in os.listdir('.'):
	lxnxpattern = lxnxfilePattern.search(old_file)

	if lxnxpattern == None:
		continue

	# Pulls the base file name and adjusts the numbering
	base_name = lxnxpattern.group(1)
	new_number = str(int(lxnxpattern.group(2)) + start_number)

	# Forms the new file name
	new_filename = base_name + new_number + '.txt'

	# Get the full absolute, file paths
	absWorkingDir = os.path.abspath('.')
	old_file = os.path.join(absWorkingDir, old_file)
	absRenumbered = os.path.join(absWorkingDir, 'Renumbered')
	new_filename = os.path.join(absRenumbered, new_filename)

	# Rename the files
	print('Renaming "%s" to "%s"...' % (old_file, new_filename))
	shutil.move(old_file, new_filename) #uncomment after testing

print('Done.')
