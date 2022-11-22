from os.path import exists
from init import globals

def check_file_exists(filename):
	if not exists(filename):
		print(globals.Red + "Manifest file is not available! ({filename})\nCheck the file and try again!" + globals.White)
		exit(1)
	return True

def read_file_content(filename):
	if check_file_exists(filename=filename):
		file = open(filename, 'r')
		content = file.read()
		file.close()
		return content
	exit(1)