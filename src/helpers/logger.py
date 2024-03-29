from init import globals
from datetime import date, datetime

def get_time_stamp():
	now = date.today()
	timestamp = now.strftime("%Y/%m/%d")
	timestamp += " - "
	timestamp += datetime.now().strftime("%H:%M:%S")
	return timestamp

def logger(level: int, email: str):
	line = '[' + get_time_stamp() + '] '
	if level == globals.EMAIL_ERROR:
		line += 'EMAIL_ERROR\t\t\t\t: invalid email address: (' + email + ')'
	elif level == globals.PASS_ERROR:
		line += 'PASS_ERROR\t\t\t\t: invalid password: (' + email + ')'
	elif level == globals.PROXY_ERROR:
		line += 'PROXY_ERROR\t\t\t\t: invalid proxy address: (' + email + ')'
	elif level == globals.CAPTCHA_ERROR:
		line += 'CAPTCHA_ERROR\t\t\t: Captcha error accured!'
	elif level == globals.BLOCKED_ACC_ERROR:
		line += 'BLOCKED_ACC_ERROR\t\t: account is temporarily blocked: (' + email + ')'
	elif level == globals.VERIFICATION_ERROR:
		line += 'VERIFICATION_ERROR\t\t: account requires verifcation: (' + email + ')'
	else:
		line += 'Unknown error\t\t\t: (' + email + ')'
	line += '\n'
	logfile = open(globals.LOG_FILE, 'a+')
	logfile.write(line)
	logfile.close()