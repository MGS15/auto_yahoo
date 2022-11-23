# -*- coding: utf-8 -*-
"""
	@Author:	Soufiane Elkhamlichi
	@Date:		11/08/2022
	@Credit:	Soufiane Elkhamlichi
	@Links:		https://github.com/MGS15/
"""

from app import route
from init import globals
import time

def init_app():
	globals.create_logfile()
	route.route()
	time.sleep(10)

def main():
	init_app()

if __name__ == "__main__":
	main()