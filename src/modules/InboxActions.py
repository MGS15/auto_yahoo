import init.globals as globals

class InboxActions:
	def __init__(self):
		self.reply = 90
		self.archive = 90
		self.star = 90
		self.replyMessage = ""
	
	# Getters
	def getReply(self):
		return self.reply
	def getArchive(self):
		return self.archive
	def getStar(self):
		return self.star
	def getReplyMessage(self):
		return self.replyMessage
	# Setters
	def setReply(self, reply: int):
		if reply in range(0, 100):
			self.reply = reply
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)
	def setArchive(self, archive: int):
		if archive in range(0, 100):
			self.archive = archive
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)
	def setStar(self, star: int):
		if star in range(0, 100):
			self.star = star
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)
	def setReplyMessage(self, message: str):
		self.replyMessage = message