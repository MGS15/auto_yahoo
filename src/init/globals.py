import os.path
from os.path import exists
from os import mkdir

# Colors
ForGround = '-ForegroundColor'
Black = ForGround + ' ' + "Black"        # Black
White = ForGround + ' ' + "White"        # White
Red = ForGround + ' ' + "Red"          # Red
Green = ForGround + ' ' + "Green"        # Green
Yellow = ForGround + ' ' + "Yellow"       # Yellow
Blue = ForGround + ' ' + "Blue"         # Blue
BBlack = ForGround + ' ' + "DarkGray"       # Black
BRed = ForGround + ' ' + "DarkRed"         # Red
BGreen = ForGround + ' ' + "DarkGreen"       # Green

# PATHS
ASSETS = "assets"
STORAGE = "storage" + os.path.sep
DRIVER_PATH = ASSETS + os.path.sep + "chromedriver.exe"
RESOURCES_PATH = ASSETS + os.path.sep + "resources.csv"
LOG_FILE = STORAGE + 'logs'
MANIFEST_PATH = ASSETS + os.path.sep + "manifest.json"
SCRIPT_PATH = ASSETS + os.path.sep + "background.js"
REPLY_PATH = ASSETS + os.path.sep + "reply_message.txt"

# Errors
EMAIL_ERROR = 1
PASS_ERROR = 2
PROXY_ERROR = 3
CAPTCHA_ERROR = 4
BLOCKED_ACC_ERROR = 5
UNKNOWN_ERROR = 6
VERIFICATION_ERROR = 7

# Spam Actions
SA_RESTORE_TO_INBOX = 'restore_to_inbox'
SA_MOVE_TO_INBOX = 'move_to_inbox'
SA_NOT_SPAM = 'not_spam'

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