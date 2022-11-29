from init import globals as globals, init_webdriver as init_webdriver, init_config as init_config, init_accounts, init_config
from app import account_spam_handler, account_inbox_handler, specifiers
from modules.Account import Account
from modules.Config import Config
import threading
import time

def route(account: Account, config: Config):
	chwd = init_webdriver.init_webdriver(account=account)
	chwd.get('https://www.yahoo.com/')
	specifiers.load_cookies(account.getEmail().split('@')[0], chwd)
	chwd.get("https://login.yahoo.com/")
	account_spam_handler.login(chwd, config, account)
	chwd.get("https://mail.yahoo.com/")
	try:
		account_spam_handler.goto_folder(chwd, config, account, 'Spam')
	except:
		chwd.refresh()
		specifiers.wait_for_specific_time(100, 200)
		account_spam_handler.goto_folder(chwd, config, account, 'Spam')
	specifiers.wait_for_specific_time(40, 50)
	pos = 3
	msgs_num = specifiers.get_number_of_msgs(chwd)
	while pos < msgs_num:
		if account_spam_handler.goto_message(chwd, config, pos):
			specifiers.wait_for_specific_time(30, 50)
			account_spam_handler.perform_spam_actions(chwd, config, account)
			specifiers.wait_for_specific_time(20, 35)
			msgs_num = specifiers.get_number_of_msgs(chwd)
			pos -= 1
		pos += 1
	print(globals.Green + "✔️  Done with spam!" + globals.White)
	try:
		account_spam_handler.goto_folder(chwd, config, account, 'Inbox')
	except:
		chwd.refresh()
		specifiers.wait_for_specific_time(100, 200)
		account_spam_handler.goto_folder(chwd, config, account, 'Inbox')
	specifiers.wait_for_specific_time(40, 80)
	pos = 3
	msgs_num = specifiers.get_number_of_msgs(chwd)
	while pos < msgs_num:
		if account_spam_handler.goto_message(chwd, config, pos):
			specifiers.wait_for_specific_time(30, 50)
			account_inbox_handler.inbox_actions_handler(chwd, config, account)
			specifiers.wait_for_specific_time(20, 35)
			account_spam_handler.goto_folder(chwd, config, account, 'Inbox')
			msgs_num = specifiers.get_number_of_msgs(chwd)
		pos +=1
	specifiers.save_cookies(account.getEmail().split('@')[0], chwd)

def entry_point():
	globals.init_storage()
	accounts = init_accounts.read_csv()
	config = init_config.getInputs()
	threads_num = config.getNumberOfThreads()
	accounts_num = len(accounts)
	threads = []
	i = 0
	while (i < accounts_num):
		for j in range(threads_num):
			if i >= accounts_num:
				break
			t = threading.Thread(target=route, args=(accounts[i], config))
			t.start()
			threads.append(t)
			i+= 1
		time.sleep(1)
		for tt in threads:
			tt.join()