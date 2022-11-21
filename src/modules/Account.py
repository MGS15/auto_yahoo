import init.globals as globals
import re

class Account:
	def __init__(self):
		self.email = ""
		self.password = ""
		self.proxyIp = ""
		self.proxyPort = ""
		self.proxyUser = ""
		self.proxyPassword = ""

	# Getters
	def getEmail(self):
		return self.email
	def getPassword(self):
		return self.password
	def getProxyIp(self):
		return self.proxyIp
	def getProxyPort(self):
		return self.proxyPort
	def getProxyUser(self):
		return self.proxyUser
	def getProxyPassword(self):
		return self.proxyPassword
	
	# Setters
	def setEmail(self, email):
		if re.fullmatch("[a-zA-Z0-9]{2,50}[\-|_|\.]*[a-zA-Z0-9]{2,50}@yahoo{1}(\.[a-zA-Z]{2,4}){1,2}", email) == None:
			raise Exception(globals.Red + "All emails should be valid!" + globals.White)
		else:
			self.email = email
	def setPassword(self, password):
		if password == "" or password == None:
			raise Exception(globals.Red + "Email password is empty!" + globals.White)
		else:
			self.password = password
	def setProxyIp(self, proxyIp):
		if re.fullmatch('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', proxyIp) == None:
			raise Exception(globals.Red + "Proxy must be valid!" + globals.White)
		else:
			self.proxyIp = proxyIp
	def setProxyPort(self, port: int):
		if port in range(0, 65535):
			self.proxyPort = port
		else:
			raise Exception(globals.Red + "Proxy's port must be between 0 and 65535!" + globals.White)
	def setProxyUser(self, username):
		if username == "" or username ==None:
			raise Exception(globals.Red + "Proxy user must be specified!" + globals.White)
		else:
			self.proxyUser = username
	def setProxyPassword(self, password):
		if password == "" or password == None:
			raise Exception(globals.Red + "Proxy password must be specified!" + globals.White)
		else:
			self.proxyPassword = password