from helpers import randomize
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.Config import Config
from selenium.webdriver.common.by import By

def write_humanly(text: str, element: WebElement):
	element.clear()
	for char in text:
		randomize.random_wait_time(1, 3)
		element.send_keys(char)

def wait_for_element_by_id(id: str, config: Config, browser: webdriver.Chrome):
	WebDriverWait(browser, config.getTimeOut()).until(
		EC.presence_of_element_located((By.ID, id))
		)

def wait_for_specific_time(min, max):
	randomize.random_wait_time(min, max)