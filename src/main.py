# -*- coding: utf-8 -*-
"""
	@Author:	Soufiane Elkhamlichi
	@Date:		11/08/2022
	@Credit:	Soufiane Elkhamlichi
	@Links:		https://github.com/MGS15/
"""

from app import route
from init import globals, init_accounts
import time

def main():
	globals.init_storage()
	accounts = init_accounts.read_csv()
	route.route(accounts[0])
	time.sleep(900000)

if __name__ == "__main__":
	main()