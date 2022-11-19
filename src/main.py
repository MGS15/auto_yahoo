# -*- coding: utf-8 -*-
"""
	@Author:	Soufiane Elkhamlichi
	@Date:		11/08/2022
	@Credit:	Soufiane Elkhamlichi
	@Links:		https://github.com/MGS15/
"""

import init.globals as globals
import app.user_input as user_input
import init.webdriver as wd
import time
import traceback

def test():
	try:
		driver = wd.init_webdriver()
		driver.get('https://mail.yahoo.com/')
		time.sleep(30)
		driver.quit()
	except Exception as e:
		print(globals.Red + "Error accured!" + globals.White)
		traceback.print_exc()

def init_app():
	user_input.get_cvs_filename("Enter CVS file (email | password | proxy | port | user | password): ")

def main():
	init_app()

if __name__ == "__main__":
	main()