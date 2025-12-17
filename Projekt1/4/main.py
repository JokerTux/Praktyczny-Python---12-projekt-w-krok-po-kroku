import sys
import os
from pathlib import Path


BLOCKED_SOURCE_TXT = []
### Please make sure you insert only strings (not ints)
BLOCKED_SOURCE_CHARS = ['#']
KNOWN_EXT = {
"#include" : "C/C++",
"#define" : "C/C++",
"<?php" : "php",
"def " : "Python",
"from " : "Python",
"import" : "Python",
"<htm" : "html",
"<body" : "html",
"<div" : "html"
}

#### os.walk ####
def v1_walk(path):
	walk = os.walk(path)
	line_ct = 0
	valid_line_list = []
	
	for dir_path, dir_name, file_names in walk:
		#print(f"dir_path : {dir_path}\ndir_name : {dir_name}\nfile_names: {file_names}")
		for file_name in file_names:
			
			if dir_path[-1] != "/":
				dir_path = dir_path + '/'

			export_path = f"{dir_path}{file_name}"
			lines_coutner(export_path, valid_line_list)

	line_ct += len(valid_line_list)
	valid_line_list = []	
	print(f"{line_ct}")		


#### I wont change the name of the function but imagine that the function has a cool descriptive name :) ####
def lines_coutner(in_path, valid_line_list):
	with open(in_path, 'r', encoding="ibm437") as f:
		files_con = f.read()
		files_con_l = files_con.splitlines()
		
		for line in files_con_l:
			line = line.strip()
			words = line.split()
			for word in words:	
				if word in KNOWN_EXT:
					print(f"{in_path} : {KNOWN_EXT[word]}")
					return

	
#### Path verification ####
def path_verification(path):
	dir_ver = os.path.isdir(path)
	
	if dir_ver:
		return True
	return False


def main():
	path = str(sys.argv[1])

	if path_verification(path):
	#### verion 1 = os.walk ####
		print("========== os.walk ==========")
		v1_walk(path)
	else:
		raise Exception("Path is not valid")
		

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise Exception("usage: args.py <path>")

	main()
