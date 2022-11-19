import init.globals as globals

class SpamActions:
	def __init__(self):
		self.read = True
		self.scroll = True
		self.restoreInbox = 50
		self.moveToInbox = 30
		self.notSpam = 20
	
	# Getters
	def getRead(self):
		return self.read
	def getScroll(self):
		return self.scroll
	def getRestoreInbox(self):
		return self.restoreInbox
	def getMoveToInbox(self):
		return self.moveToInbox
	def getMoveToInbox(self):
		return self.moveToInbox
	def getNotSpam(self):
		return self.notSpam
	# Setters
	def setRead(self, value: bool):
		self.read = value
	def setScroll(self, value: bool):
		self.scroll = value
	def setRestoreInbox(self, value: int):
		if value in range(0, 100):
			self.restoreInbox = value
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)
	def setMoveToInbox(self, value: int):
		if value in range(0, 100):
			self.moveToInbox = value
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)
	def setNotSpam(self, value: int):
		if value in range(0, 100):
			self.notSpam = value
		else:
			raise Exception(globals.Red + "This action requires a value between 0 and 100!" + globals.White)