import init.globals as globals
import undetected_chromedriver as uc
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

def init_webdriver():
	ua = UserAgent()
	userAgent = ua.random
	chrm_opt = Options()
	chrm_opt.add_argument("--lang={}".format("en"))
	chrm_opt.add_argument(f'user-agent={userAgent}')
	driver = uc.Chrome(chrome_options=chrm_opt, executable_path=globals.DRIVER_PATH)
	return driver