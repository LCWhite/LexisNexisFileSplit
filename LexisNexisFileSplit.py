#! /usr/bin/env python3
# LexisNexisFunctionsSplot.py takes a text file output of LexisNexis search
# results, splits it into individual files for each article included
# in the search output, numbers them, and saves them to a new folder.


import re, os


input_file = input("Enter file name: ")
file_name = input("Enter base name for all of the files to be subset: ")

new_folder = 'LexisNexis_Article_Files'
os.makedirs(new_folder)


def lexinexis_filesplit(input_file, file_name):
	"""
	Takes LexisNexis Full-Text Document export and splits it into individual
	files

	"""
	f_read = open(input_file)
	count = 0
	f_write = open(os.path.join(new_folder, file_name + str(count) + '.txt'), 'w')
	for line in f_read:
		if re.search('\d* of \d* DOCUMENT', line):
			f_write.close()
			count = count + 1
			f_write = open(os.path.join(new_folder, file_name + "_" + str(count) + '.txt'), 'w')
			f_write.write(line)

		else:
			f_write.write(line)

			# Adds error message if numbered files are missing from the LexisNexis text file
			if re.search('This document could not be formatted for delivery', line):
				print('''There may be a missing document, please check
				and make sure document ''' + str(count + 1) + ' is accounted for.')

				# Full LexisNexis error message is:
				# "This document could not be formatted for delivery. If your
				# delivery request included other documents,
				# they completed successfully."

	f_write.close()
	f_read.close()

lexinexis_filesplit(input_file, file_name)
print('Done.')

#TODO: Add an option to zip files at the end
