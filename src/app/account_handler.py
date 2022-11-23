from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import traceback
from modules.Config import Config
from modules.Account import Account
from app import specifiers
from init import globals

def login(browser: webdriver.Chrome, config: Config, account: Account):
	try:
		specifiers.wait_for_element_by_id('login-username', config, browser)
		element = browser.find_element(By.ID, 'login-username')
		specifiers.write_humanly(account.getEmail(), element)
		specifiers.wait_for_element_by_id('login-signin', config, browser)
		specifiers.wait_for_specific_time(20, 30)
		element = browser.find_element(By.ID, 'login-signin')
		element.send_keys(Keys.ENTER)
		specifiers.wait_for_specific_time(20, 30)		
	except:
		print(globals.Red + "Error while waiting for user to login..." + globals.White)
		traceback.print_exc()
	