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

def write_text_input(browser: webdriver.Chrome, timeout: int, text: str, id: str):
	try:
		specifiers.wait_for_element_by_id(id, timeout, browser)
		element = browser.find_element(By.ID, id)
		specifiers.write_humanly(text, element)
	except:
		raise Exception(globals.Red + f"Error while waiting for element {id}..." + globals.White)

def send_key_to_elem(browser: webdriver.Chrome, timeout: int, key, id: str):
	try:
		specifiers.wait_for_element_by_id(id, timeout, browser)
		element = browser.find_element(By.ID, id)
		element.send_keys(key)
	except:
		raise Exception(globals.Red + f"Error while waiting for element {id}..." + globals.White)

def login(browser: webdriver.Chrome, config: Config, account: Account):
	try:
		write_text_input(browser, config.getTimeOut(), account.getEmail(), 'login-username')
		send_key_to_elem(browser, config.getTimeOut(), Keys.ENTER, 'login-signin')
		specifiers.wait_for_specific_time(20, 30)
	except:
		print(globals.Red + "Error while waiting for user to login..." + globals.White)
		traceback.print_exc()
		browser.quit()
	try:
		browser.find_element(By.ID, 'username-error')
		print(globals.Red + "Email address error..." + globals.White)
		logger.logger(globals.EMAIL_ERROR, account.getEmail())
		browser.quit()
	except:
		pass
	try:
		# specifiers.wait_for_specific_time(50, 100)
		print(globals.BRed + "test 1" + globals.White)
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.frame_to_be_available_and_switch_to_it(browser.find_element(By.ID, 'recaptcha-iframe'))
		)
		# print(browser.page_source)
		# print(browser.find_elements(By.TAG_NAME, 'iframe')[0].)
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.frame_to_be_available_and_switch_to_it(browser.find_elements(By.TAG_NAME, 'iframe')[0])
		)
		# print(browser.page_source)
		print(globals.BRed + "test 2" + globals.White)
		WebDriverWait(browser, config.getTimeOut()).until(
			EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
		)
		print(globals.BRed + "test 2.5" + globals.White)
		element = browser.find_element(By.XPATH, '/html/body/div/div[3]/div/div/div/span')
		print(globals.BRed + "test 3" + globals.White)
		element.click()
		print(globals.BRed + "test 4" + globals.White)
		specifiers.wait_for_specific_time(30, 50)
		print(globals.BRed + "test 5" + globals.White)
		element = browser.find_element(By.ID, 'recaptcha-submit')
		print(globals.BRed + "test 6" + globals.White)
		element.send_keys(Keys.ENTER)
		print(globals.BRed + "test 7" + globals.White)
		specifiers.wait_for_specific_time(30, 50)
		print(globals.BRed + "test 8" + globals.White)
	except:
		print(globals.Red + "reCaptcha error..." + globals.White)
		# traceback.print_exc()