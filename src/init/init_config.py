import modules.Config as Config
from init import globals

def inputStrings(prompt: str):
	errColor = globals.BBlack
	inputVal = ""
	while True:
		inputVal = input(errColor + prompt + globals.White)
		if inputVal != "" and inputVal != None:
			break ;
		else:
			errColor = globals.Red
	return inputVal

def inputInt(promt: str, min: int, max: int):
	errColor = globals.BBlack
	inputVal = -1
	while True:
		try:
			inputVal = int(input(errColor + promt + globals.White))
		except:
			errColor = globals.Red
			print(errColor + "Expecting a digit!" + globals.White)
			continue ;
		if (inputVal > min and inputVal < max):
			break ;
		else:
			errColor = globals.Red
	return inputVal


def getInputs():
	config = Config.Config()
	config.setEmailFrom(inputStrings("Enter email from: "))
	config.setEmailSubject(inputStrings("Enter email subject: "))
	config.setTimeout(int(inputInt("Enter timeout value: ", 0, 18000)))
	config.setNumberOfThreads(int(inputInt("Enter number of threads: ", 0, 50)))
	return config
	