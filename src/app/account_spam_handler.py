from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.Config import Config
from modules.Account import Account
from app import specifiers
from init import globals
from helpers import logger, randomize

def reCaptcha_handler(browser: webdriver.Chrome, timeout: int):
	while True:
		try:
			specifiers.wait_for_element_by_id('login-passwd', timeout, browser)
			break
		except:
			continue

def login(browser: webdriver.Chrome, config: Config, account: Account):
	try:
		specifiers.write_text_input(browser, config.getTimeOut(), account.getEmail(), 'login-username')
		specifiers.send_key_to_elem(browser, config.getTimeOut(), Keys.ENTER, 'login-signin')
		specifiers.wait_for_specific_time(30, 80)
	except:
		print(globals.Red + "Error while waiting for user to login..." + globals.White)
		logger.logger(globals.UNKNOWN_ERROR, '', account.getEmail())
		browser.quit()
	try:
		browser.find_element(By.ID, 'username-error')
		print(globals.Red + "Email address error..." + globals.White)
		logger.logger(globals.EMAIL_ERROR, account.getEmail())
		browser.quit()
	except:
		pass
	reCaptcha_handler(browser=browser, timeout=config.getTimeOut())
	try:
		specifiers.write_text_input(browser, config.getTimeOut(), account.getPassword(), 'login-passwd')
		specifiers.send_key_to_elem(browser, config.getTimeOut(), Keys.ENTER, 'login-signin')
		specifiers.wait_for_specific_time(30, 80)
	except:
		print(globals.Red + "Error while waiting for password..." + globals.White)
		logger.logger(globals.UNKNOWN_ERROR, '', account.getEmail())
		browser.quit()
	specifiers.wait_for_specific_time(30, 80)
	try:
		browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/p')
		print(globals.Red + "Invalid password..." + globals.White)
		logger.logger(globals.PASS_ERROR, account.getEmail())
		browser.quit()
	except:
		pass
	print(f"{globals.Green}{account.getEmail()}✔️  logged in!{globals.White}")

def goto_folder(browser: webdriver.Chrome, config: Config, account: Account, folder: str):
	pos = 0
	while (pos:=pos+1):
		xpath = f'/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/nav/div/div[3]/div[1]/ul/li[{pos}]'
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.presence_of_element_located((By.XPATH, xpath))
			)
		element = browser.find_element(By.XPATH, xpath)
		if element.text == folder:
			element.click()
			return
		else:
			if pos > 9:
				break
	logger.logger(globals.UNKNOWN_ERROR, account.getEmail())
	raise Exception(globals.Red + f"Could not loccate the folder named '{folder}'!" + globals.White)
	
def goto_message(browser: webdriver.Chrome, config: Config, pos: int):
	xpathfrom = f'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div[1]/ul/li[{pos}]/a/div/div[1]/div[2]/span'
	xpathsubj = f'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div[1]/ul/li[{pos}]/a/div/div[2]/div[1]/div[1]/span[1]'
	try:
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.presence_of_element_located((By.XPATH, xpathfrom))
			)
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.presence_of_element_located((By.XPATH, xpathfrom))
			)
	except:
		return False
	fromname = browser.find_element(By.XPATH, xpathfrom)
	subject = browser.find_element(By.XPATH, xpathsubj)
	if fromname.text == config.getEmailFrom() and subject.text == config.getEmailSubject():
		subject.click()
		return True
	else:
		return False

def perform_spam_actions(browser: webdriver.Chrome, config: Config, email: str):
	try:
		xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]'
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.presence_of_element_located((By.XPATH, xpath))
			)
		specifiers.scroll_down_inner_scrollbar(browser, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]')
		actions = spam_actions_handler(config)
		rd = randomize.random_num_in_range(0, len(actions) - 1)
		if actions[rd] == globals.SA_RESTORE_TO_INBOX:
			raw_spam_action(
				browser,
				config.getTimeOut(),
				'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[1]/div/button'
				)
		elif actions[rd] == globals.SA_MOVE_TO_INBOX:
			raw_spam_action(
				browser,
				config.getTimeOut(),
				'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[2]/div/span/button'
				)
			specifiers.wait_for_specific_time(10, 25)
			raw_spam_action(
				browser,
				config.getTimeOut(),
				'/html/body/div[1]/div/div[1]/div/div[7]/div/div[1]/div/div/ul[2]/div/ul[1]/li[1]/button'
				)
		else:
			raw_spam_action(
				browser,
				config.getTimeOut(),
				'/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[4]/div/button'
				)
	except:
		print(globals.Red + "Unknown error..." + globals.White)
		logger.logger(globals.PASS_ERROR, email)
		browser.quit()

def spam_actions_handler(config: Config):
	restore_to_inbox = config.spamActions.getRestoreInbox()
	move_to_inbox = config.spamActions.getMoveToInbox()
	not_spam = config.spamActions.getNotSpam()
	i = 0
	actions = []
	while i < restore_to_inbox:
		actions.append(globals.SA_RESTORE_TO_INBOX)
		i += 1
	while i < move_to_inbox + restore_to_inbox:
		actions.append(globals.SA_MOVE_TO_INBOX)
		i += 1
	while i < not_spam + move_to_inbox + restore_to_inbox:
		actions.append(globals.SA_NOT_SPAM)
		i += 1
	return actions

def raw_spam_action(browser: webdriver.Chrome, timeout: int, xpath: str):
	WebDriverWait(browser, timeout).until(
		EC.presence_of_element_located((By.XPATH, xpath))
	)
	element = browser.find_element(By.XPATH, xpath)
	element.click()
