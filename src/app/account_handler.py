from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import traceback
from modules.Config import Config
from modules.Account import Account
from app import specifiers
from init import globals
from helpers import logger

def login(browser: webdriver.Chrome, config: Config, account: Account):
	try:
		specifiers.wait_for_element_by_id('login-username', config, browser)
		element = browser.find_element(By.ID, 'login-username')
		specifiers.write_humanly(account.getEmail(), element)
		specifiers.wait_for_element_by_id('login-signin', config, browser)
		element = browser.find_element(By.ID, 'login-signin')
		element.send_keys(Keys.ENTER)
		specifiers.wait_for_specific_time(20, 30)
		try:
			browser.find_element(By.ID, 'username-error')
			print(globals.Red + "Email address error..." + globals.White)
			logger.logger(globals.EMAIL_ERROR, account.getEmail())
			browser.quit()
		except:
			pass
		specifiers.wait_for_specific_time(200, 300)
	except:
		print(globals.Red + "Error while waiting for user to login..." + globals.White)
		traceback.print_exc()
		browser.quit()
	