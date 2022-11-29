from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from modules.Config import Config
from modules.Account import Account
from app import specifiers
from init import globals
from helpers import logger, randomize

def inbox_actions_handler(browser: webdriver.Chrome, config: Config, account:  Account):
	specifiers.scroll_down_inner_scrollbar(browser, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]')
	choice = randomize.random_num_in_range(0, 100)
	if choice in range(0, config.inboxActions.getStar()):
		try:
			star(browser, config.getTimeOut())
		except:
			print(globals.Red + 'Error while trying to star' + globals.White)
	specifiers.wait_for_specific_time(30, 50)
	choice = randomize.random_num_in_range(0, 100)
	if choice in range(0, config.inboxActions.getReply()):
		try:
			reply(browser, config.getTimeOut(), config.inboxActions.getReplyMessage())
		except:
			print(globals.Red + 'Error while trying to reply' + globals.White)
	specifiers.wait_for_specific_time(30, 50)
	choice = randomize.random_num_in_range(0, 100)
	if choice in range(0, config.inboxActions.getArchive()):
		try:
			archive(browser, config.getTimeOut())
		except:
			print(globals.Red + 'Error while trying to archive' + globals.White)


def star(browser: webdriver.Chrome, timeout: int):
	upper_star = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/header/div[3]/div[2]/button'
	lower_star = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li/div/div[1]/header/div[5]/button'
	more_act = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[5]/div/div/button'
	sub_more = '/html/body/div[1]/div/div[1]/div/div[7]/div/div[1]/div/div/ul/li[2]/a'
	choice = randomize.random_num_in_range(1, 15)
	if choice <= 5:
		raw_action(browser, timeout, upper_star)
	elif choice <= 10:
		raw_action(browser, timeout, lower_star)
	else:
		raw_action(browser, timeout, more_act)
		specifiers.wait_for_specific_time(15, 30)
		raw_action(browser, timeout, sub_more)

def reply(browser: webdriver.Chrome, timeout: int, reply_msg: str):
	upper_reply = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[1]/button'
	lower_reply = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li/div/div[2]/div[2]/div/div/ul/li[1]/span/button'
	rply_button = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/div/div/ul/span/li[1]/button'
	send_reply = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li[2]/div/div/div[2]/div[2]/div/button'
	choice = randomize.random_num_in_range(0, 100)
	if choice <= 5:
		raw_action(browser, timeout, upper_reply)
	elif choice <= 10:
		raw_action(browser, timeout, lower_reply)
	else:
		raw_action(browser, timeout, rply_button)
	text_area = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div[2]/ul/li[2]/div/div/div[2]/div[1]/div/div[2]/div/div[1]'
	WebDriverWait(browser, timeout).until(
		EC.presence_of_element_located((By.XPATH, text_area))
	)
	element = browser.find_element(By.XPATH, text_area)
	element.clear()
	specifiers.write_humanly(reply_msg, element)
	WebDriverWait(browser, timeout).until(
		EC.presence_of_element_located((By.XPATH, send_reply))
	)
	element = browser.find_element(By.XPATH, send_reply)
	specifiers.wait_for_specific_time(15, 30)
	element.click()


def archive(browser: webdriver.Chrome, timeout: int):
	archieve_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[1]/div/button'
	moveto_archive = '/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/ul/li[2]/div/span/button'
	sub_archive = '/html/body/div[1]/div/div[1]/div/div[7]/div/div[1]/div/div/ul[2]/div/ul[1]/li[2]/button'
	choice = randomize.random_num_in_range(0, 100)
	if choice % 2:
		raw_action(browser, timeout, archieve_xpath)
	else:
		raw_action(browser, timeout, moveto_archive)
		specifiers.wait_for_specific_time(15, 30)
		raw_action(browser, timeout, sub_archive)

def raw_action(browser: webdriver.Chrome, timeout: int, xpath: str):
	WebDriverWait(browser, timeout).until(
			EC.presence_of_element_located((By.XPATH, xpath))
		)
	element = browser.find_element(By.XPATH, xpath)
	element.click()
