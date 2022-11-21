import init.globals as globals
from modules import InboxActions, SpamActions

class Config:
	spamActions = SpamActions.SpamActions()
	inboxActions = InboxActions.InboxActions()
	def __init__(self):
		self.emailFrom = ""
		self.emailSubject = ""
		self.timeOut = 1000
		self.numberOfThreads = 1
	
	# Getters
	def getEmailFrom(self):
		return self.emailFrom
	def getEmailSubject(self):
		return self.emailSubject
	def getTimeOut(self):
		return self.timeOut
	def getNumberOfThreads(self):
		return self.numberOfThreads
	
	# Setters
	def setEmailFrom(self, emailFrom: str):
		self.emailFrom = emailFrom
	def setEmailSubject(self, emailSubject: str):
		self.emailSubject = emailSubject
	def setTimeout(self, timeout: int):
		if timeout > 0 and timeout < 180000:
			self.timeOut = timeout
		else:
			raise Exception(globals.Red + "Time out value must be between 1 sec and 3 min!" + globals.White)
	def setNumberOfThreads(self, numberOfThreads: int):
		if numberOfThreads > 0 and numberOfThreads < 50:
			self.numberOfThreads = numberOfThreads
		else:
			raise Exception(globals.Red + "Time out value must be between 1 and 50!" + globals.White)