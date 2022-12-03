from helpers import randomize
from init import globals
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers import logger
import json
import os
import traceback

def write_humanly(text: str, element: WebElement):
	element.clear()
	for char in text:
		randomize.random_wait_time(1, 3)
		element.send_keys(char)

def wait_for_element_by_id(id: str, timeout: int, browser: webdriver.Chrome):
	WebDriverWait(browser, timeout).until(
		EC.presence_of_element_located((By.ID, id))
		)

def wait_for_specific_time(min, max):
	randomize.random_wait_time(min, max)

def write_text_input(browser: webdriver.Chrome, timeout: int, text: str, id: str):
	try:
		wait_for_element_by_id(id, timeout, browser)
		element = browser.find_element(By.ID, id)
		write_humanly(text, element)
	except:
		raise Exception(globals.Red + f"Error while waiting for element {id}..." + globals.White)

def send_key_to_elem(browser: webdriver.Chrome, timeout: int, key, id: str):
	try:
		wait_for_element_by_id(id, timeout, browser)
		element = browser.find_element(By.ID, id)
		element.send_keys(key)
	except:
		raise Exception(globals.Red + f"Error while waiting for element {id}..." + globals.White)

def save_cookies(uname: str, browser: webdriver.Chrome):
	with open(f'{globals.STORAGE}{uname}{os.path.sep}cookies.json', 'w') as cf:
		json.dump(browser.get_cookies(), cf)

def load_cookies(uname: str, browser: webdriver.Chrome):
	if not os.path.exists(f'{globals.STORAGE}{uname}{os.path.sep}cookies.json'):
		return
	cookies = []
	with open(f'{globals.STORAGE}{uname}{os.path.sep}cookies.json', 'r') as cf:
		try:
			cookies += json.load(cf)
		except:
			print('Cookies file error')
	for cookie in cookies:
		try:
			browser.add_cookie(cookie)
		except:
			pass
	browser.refresh()

def scroll_down_inner_scrollbar(browser: webdriver.Chrome, xpath: str):
	element = browser.find_element(By.XPATH, xpath)
	scroll = 0
	while scroll < 4:
		browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', element)
		scroll += 1
		wait_for_specific_time(10, 40)

def get_number_of_msgs(browser: webdriver.Chrome) -> int:
	elements = browser.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div/div[1]/ul/li')
	return len(elements)

def account_errors_hanlder(browser: webdriver.Chrome, timeout: int, _id: str):
	try:
		wait_for_element_by_id(_id, timeout, browser)
		return True
	except:
		return False