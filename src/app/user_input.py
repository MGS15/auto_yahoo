import init.globals as globals

def get_user_input(prompt: str):
	init_color = globals.BBlack
	uinput = ""
	while True:
		uinput = input(init_color + prompt + globals.White)
		if uinput != "":
			break
		else:
			init_color = globals.Red
	return uinput

def get_cvs_filename(prompt: str):
	cvs_file = get_user_input(prompt=prompt)
	print(cvs_file)
