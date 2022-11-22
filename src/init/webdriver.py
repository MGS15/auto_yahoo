import init.globals as globals
from helpers import readfiles
from modules.Account import Account
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import zipfile

def create_extention(manifist, script, filename):
	with zipfile.ZipFile(filename, 'w') as ext:
		ext.writestr("manifest.json", manifist)
		ext.writestr("background.js", script)

def chrome_proxy(account: Account):
	manifist_json = readfiles.read_file_content(globals.MANIFEST_PATH)
	background_js = readfiles.read_file_content(globals.SCRIPT_PATH) % {
            "host": account.getProxyIp(),
            "port": account.getProxyPort(),
            "user": account.getProxyUser(),
            "pass": account.getProxyPassword(),
        }
	ex_name = globals.STORAGE + account.getEmail().split('@')[0] + "_proxy_extention.zip"
	create_extention(manifist_json, background_js, ex_name)
	return ex_name

def init_webdriver(account: Account):
	ua = UserAgent()
	plugin_file = chrome_proxy(account)
	userAgent = ua.random
	chrm_opt = Options()
	chrm_opt.add_argument("--lang={}".format("en"))
	chrm_opt.add_argument('--disable-gpu')
	chrm_opt.add_argument('--disable-infobars')
	chrm_opt.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
	chrm_opt.add_argument(f'user-agent={userAgent}')
	chrm_opt.add_extension(plugin_file)
	driver = uc.Chrome(chrome_options=chrm_opt, executable_path=globals.DRIVER_PATH)
	return driver