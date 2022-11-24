from init import globals as globals, init_webdriver as init_webdriver, init_config as init_config, init_accounts, init_config
from app import account_handler
import time
import traceback

def route():
	try:
		accounts = init_accounts.read_csv()
		config = init_config.getInputs()
		chwd = init_webdriver.init_webdriver(account=accounts[0])
		chwd.get("https://login.yahoo.com/")
		account_handler.login(chwd, config, accounts[0])
	except Exception as e:
		print(globals.Red + "Error accured!" + globals.White)
		traceback.print_exc()