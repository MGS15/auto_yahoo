import os.path
from os.path import exists
from os import mkdir

# Colors
Black = "\033[0;30m"        # Black
White = "\033[0;37m"        # White
Red = "\033[0;31m"          # Red
Green = "\033[0;32m"        # Green
Yellow = "\033[0;33m"       # Yellow
Blue = "\033[0;34m"         # Blue
BBlack = "\033[1;30m"       # Black
BRed = "\033[1;31m"         # Red
BGreen = "\033[1;32m"       # Green

# PATHS
ASSETS = "assets"
STORAGE = "storage" + os.path.sep
DRIVER_PATH = ASSETS + os.path.sep + "chromedriver.exe"
RESOURCES_PATH = ASSETS + os.path.sep + "resources.csv"
LOG_FILE = STORAGE + 'logs'
MANIFEST_PATH = ASSETS + os.path.sep + "manifest.json"
SCRIPT_PATH = ASSETS + os.path.sep + "background.js"

# Errors
EMAIL_ERROR = 1
PASS_ERROR = 2
PROXY_ERROR = 3
CAPTCHA_ERROR = 4
BLOCKED_ACC_ERROR = 5

def create_logfile():
	if not exists(LOG_FILE):
		log_file = open(LOG_FILE, 'w+')
		log_file.close()

def init_storage():
	if not exists(STORAGE):
		mkdir(STORAGE)
	create_logfile()

def sub_dir_storage(name: str):
	if not exists(STORAGE + name):
		mkdir(STORAGE + name)