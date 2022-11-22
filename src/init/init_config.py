import modules.Config as Config
from init import globals
from helpers import randomize

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
		if (inputVal in range(min, max)):
			break ;
		else:
			errColor = globals.Red
	return inputVal


def getInputs():
	config = Config.Config()
	config.setEmailFrom(inputStrings("Enter email from: "))
	config.setEmailSubject(inputStrings("Enter email subject: "))
	config.setTimeout(int(inputInt("Enter timeout value: ", 0, 180000)))
	config.setNumberOfThreads(int(inputInt("Enter number of threads: ", 1, 50)))
	print("Spam actions:")
	config.spamActions.setRestoreInbox(int(inputInt("\tRestore inbox ratio / 100: ", 0, 100)))
	config.spamActions.setMoveToInbox(int(inputInt("\tMove to inbox ratio / 100: ", 0, 100)))
	config.spamActions.setNotSpam(int(inputInt("\tNot spam ratio / 100: ", 0, 100)))
	print("Inbox actions:")
	config.inboxActions.setArchive(int(inputInt("\tArchive / 100: ", 0, 100)))
	config.inboxActions.setStar(int(inputInt("\tStar / 100: ", 0, 100)))
	config.inboxActions.setReply(int(inputInt("\tReply / 100: ", 0, 100)))
	config.inboxActions.setReplyMessage(input("Set custome message for reply (Leave empty to randomize): "))
	if config.inboxActions.getReplyMessage() == None or config.inboxActions.getReplyMessage() == '':
		config.inboxActions.setReplyMessage(randomize.generate_relpy_message())
	return config
	