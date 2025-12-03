import sys
import os
from pathlib import Path


BLOCKED_SOURCE_TXT = []
### Please make sure you insert only strings (not ints)
BLOCKED_SOURCE_CHARS = ['#']


#### os.listdir ####
def v3_listdir(path):
	test_fil = os.path.isfile(path)
	test_dir = path_verification(path)

	if test_fil:
		print(path)
	else:
		listdir_ls = os.listdir(path)

		for v3_file in listdir_ls:
			v3_file = os.path.join(path, v3_file)
			v3_listdir(v3_file)


#### os.pathlib ####
def v2_pathlib(path):
	pathlib_ls = Path(path)
	
	for v2_file in pathlib_ls.iterdir():
		if path_verification(v2_file):	
			v2_pathlib(v2_file)
		else:
			print(v2_file)


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


#### Lines counter ####
def lines_coutner(in_path, valid_line_list):
	with open(in_path, encoding="ibm437") as f:
		files_con = f.read()
		files_con_l = files_con.splitlines()
		
		for line in files_con_l:
			line = line.strip()
			if not line:
				pass
			elif line.startswith(tuple(BLOCKED_SOURCE_TXT)):
				#print(line)
				pass
			elif line.startswith(tuple(BLOCKED_SOURCE_CHARS)):
				#print(line)
				pass	
			else:
				#print(line)
				valid_line_list.append(line)

			# print(f"path {in_path}. len {len(line.splitlines())}")

	
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
