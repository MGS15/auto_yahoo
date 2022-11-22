from modules.Account import Account
from init import globals as globals
from helpers import readfiles
import csv
from os.path import exists

def fill_account_info(line: int, row: list):
	try:
		account = Account()
		account.setEmail(row[0])
		account.setPassword(row[1])
		account.setProxyIp(row[2])
		account.setProxyPort(int(row[3]))
		account.setProxyUser(row[4])
		account.setProxyPassword(row[5])
		return account
	except Exception as e:
		print(globals.Red + "Input error at line " + str(line) + " in resources file!" + globals.White)
		print(e)
		exit(1)

def read_csv():
	if not readfiles.check_file_exists(globals.RESOURCES_PATH):
		exit(1)
	accounts = []
	with open(globals.RESOURCES_PATH) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		next(csv_reader, None)
		line = 0
		for row in csv_reader:
			line += 1
			try:
				account = fill_account_info(line, row)
				accounts.append(account)
			except Exception as e:
				print(globals.Red + "Input error at line " + str(line) + " in resources file!" + globals.White)
				print(e)
				exit(1)
		return accounts
		
