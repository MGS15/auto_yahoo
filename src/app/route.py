from init import globals as globals, init_webdriver as init_webdriver, init_config as init_config, init_accounts, init_config
from app import account_spam_handler, specifiers

def route():
	accounts = init_accounts.read_csv()
	config = init_config.getInputs()
	chwd = init_webdriver.init_webdriver(account=accounts[0])
	chwd.get("https://login.yahoo.com/")
	specifiers.load_cookies(accounts[0].getEmail().split('@')[0], chwd)
	account_spam_handler.login(chwd, config, accounts[0])
	chwd.get("https://mail.yahoo.com/")
	account_spam_handler.goto_folder(chwd, config, accounts[0], 'Spam')
	specifiers.wait_for_specific_time(40, 50)
	pos = 3
	msgs_num = account_spam_handler.get_number_of_msgs(chwd)
	while pos < msgs_num:
		if account_spam_handler.goto_message(chwd, config, pos):
			specifiers.wait_for_specific_time(30, 50)
			account_spam_handler.perform_spam_actions(chwd, config, accounts[0])
			specifiers.wait_for_specific_time(20, 35)
			msgs_num = account_spam_handler.get_number_of_msgs(chwd)
			pos -= 1
		pos += 1
	print(globals.Green + "✔️  Done with spam!" + globals.White)
	account_spam_handler.goto_folder(chwd, config, accounts[0], 'Inbox')
	specifiers.wait_for_specific_time(40, 80)
	pos = 3
	msgs_num = account_spam_handler.get_number_of_msgs(chwd)
	specifiers.save_cookies(accounts[0].getEmail().split('@')[0], chwd)
	