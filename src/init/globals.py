import os.path
from os.path import exists

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

def create_logfile():
	if not exists(LOG_FILE):
		log_file = open(LOG_FILE, 'w+')
		log_file.write("Logs: ")