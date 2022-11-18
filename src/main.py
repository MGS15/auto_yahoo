# -*- coding: utf-8 -*-
"""
	@Author:	Soufiane Elkhamlichi
	@Date:		11/08/2022
	@Credit:	Soufiane Elkhamlichi
	@Links:		https://github.com/MGS15/
"""

import init.globals as globals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test():
	try:
		driver = webdriver.Firefox()
		driver.get("http://www.python.org")
		assert "Python" in driver.title # Nice to work with
		elem = driver.find_element(By.NAME, "q")
		elem.clear()
		elem.send_keys("This is a test")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source
		driver.close()
	except:
		print(globals.Red + "Error accured!" + globals.White)


def main():
	test()

if __name__ == "__main__":
	main()