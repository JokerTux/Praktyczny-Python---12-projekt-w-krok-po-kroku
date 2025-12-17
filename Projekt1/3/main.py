import sys
import os
from pathlib import Path

FILE_EXT_L = []
BLOCKED_SOURCE_TXT = []
## check int
BLOCKED_SOURCE_CHARS = ['#']



#### os.walk ####
def v1_walk(path):
	walk = os.walk(path)
	line_ct = 0
	valid_line_list = []	
	
	for dir_path, dir_name, file_names in walk:
		for file_name in file_names:
			file_extension = os.path.splitext(file_name)
			#print(file_extension[1])
			#print(f"fe : {file_extension}, list = {FILE_EXT_L}")
			if file_extension[1] not in FILE_EXT_L:
				if file_extension[1] == '':
					pass		
				else:
					FILE_EXT_L.append(file_extension[1])
	



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
		print(FILE_EXT_L)
	# #### verion 2 = pathlib ####
	# 	print("========== pathlib ==========")
	# 	v2_pathlib(path)
	# #### verion 3 = listdir ####
	# 	print("========== listdir ==========")
	# 	v3_listdir(path)
	else:
		raise Exception("Path is not valid")
		

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise Exception("usage: args.py <path>")

	main()
