from init import globals as globals, init_webdriver as init_webdriver, init_config as init_config, init_accounts, init_config
from app import account_handler, specifiers

def route():
	accounts = init_accounts.read_csv()
	config = init_config.getInputs()
	chwd = init_webdriver.init_webdriver(account=accounts[0])
	chwd.get("https://login.yahoo.com/")
	specifiers.load_cookies(accounts[0].getEmail().split('@')[0], chwd)
	account_handler.login(chwd, config, accounts[0])
	chwd.get("https://mail.yahoo.com/")
	account_handler.goto_folder(chwd, config, accounts[0], 'Spam')
	account_handler.goto_message(chwd, config, 3)
	account_handler.perform_spam_actions(chwd, config, accounts[0])
	