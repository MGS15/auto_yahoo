from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
from modules.Config import Config
from modules.Account import Account
from app import specifiers
from init import globals
from helpers import logger

def reCaptcha_handler(browser: webdriver.Chrome, timeout: int):
	try:
		WebDriverWait(browser, timeout).until(
			EC.frame_to_be_available_and_switch_to_it(browser.find_element(By.ID, 'recaptcha-iframe'))
		)
		color = globals.Yellow
		while True:
			_input = input(f"{color}Enter \"y/Y\" after solving and submitting reCaptcha: {globals.White}")
			if _input == "y" or _input == "Y":
				break
			else:
				color = globals.Red
		# WebDriverWait(browser, timeout).until(
		# 	EC.frame_to_be_available_and_switch_to_it(browser.find_elements(By.TAG_NAME, 'iframe')[0])
		# )
		# WebDriverWait(browser, timeout).until(
		# 	EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
		# )
		# element = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/span')
		# print(globals.BRed + "test 3" + globals.White)
		# element.click()
		# specifiers.wait_for_specific_time(30, 50)
		# browser.switch_to.default_content()
		# print(globals.BRed + "test 5" + globals.White)
		# element = browser.find_element(By.ID, 'recaptcha-submit')
		# element.send_keys(Keys.ENTER)
		# specifiers.wait_for_specific_time(30, 50)
	except:
		return False
		# traceback.print_exc()

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
	reCaptcha_handler(browser=browser, timeout=config.getTimeOut())
	try:
		browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/p')
		print(globals.Red + "Invalid password..." + globals.White)
		logger.logger(globals.PASS_ERROR, account.getEmail())
		browser.quit()
	except:
		pass

	
	