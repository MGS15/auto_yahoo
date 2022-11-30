import init.globals as globals
from helpers import readfiles
from modules.Account import Account
# import undetected_chromedriver as uc
# from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os

def create_extention(manifist, script, filename):
	manfile = None
	scrptfile = None
	if not os.path.exists(filename + os.path.sep + "manifest.json"):
		manfile = open(filename + os.path.sep + "manifest.json", 'w+')
		manfile.write(manifist)
	else:
		manfile = open(filename + os.path.sep + "manifest.json", 'w')
		manfile.write(manifist)
	if not os.path.exists(filename + os.path.sep + "background.js"):
		scrptfile = open(filename + os.path.sep + "background.js", 'w+')
		scrptfile.write(script)
	else:
		scrptfile = open(filename + os.path.sep + "background.js" , 'w')
		scrptfile.write(script)

def chrome_proxy(account: Account):
	manifist_json = readfiles.read_file_content(globals.MANIFEST_PATH)
	background_js = readfiles.read_file_content(globals.SCRIPT_PATH) % {
            "host": account.getProxyIp(),
            "port": account.getProxyPort(),
            "user": account.getProxyUser(),
            "pass": account.getProxyPassword(),
        }
	ex_name = globals.STORAGE + account.getEmail().split('@')[0] + os.path.sep + "proxy_extention"
	if not os.path.exists(ex_name):
		os.mkdir(ex_name)
	create_extention(manifist_json, background_js, ex_name)
	return ex_name

def init_webdriver(account: Account):
	# ua = UserAgent()
	# userAgent = ua.random
	plugin_file = chrome_proxy(account)
	chrm_opt = Options()
	chrm_opt.add_argument("--lang={}".format("en"))
	chrm_opt.add_argument('--disable-gpu')
	chrm_opt.add_argument('--disable-infobars')
	chrm_opt.add_experimental_option("excludeSwitches",["enable-automation"])
	chrm_opt.add_experimental_option("useAutomationExtension", False)
	chrm_opt.add_experimental_option("detach", True)
	# chrm_opt.add_argument(f'user-agent={userAgent}')
	# chrm_opt.add_argument('--load-extension=' + os.getcwd() + os.path.sep + plugin_file)
	driver = webdriver.Chrome(chrome_options=chrm_opt, executable_path=globals.DRIVER_PATH)
	print(globals.Green + "✔️  Done initializing webdriver." + globals.White)
	return driver