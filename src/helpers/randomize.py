import random
import string
import time

def random_wait_time(min: int, max: int):
	time.sleep(random.randint(min, max) / 10)

def random_num_in_range(min: int, max: int):
	return random.randint(min, max)

def generate_relpy_message():
	random_reply = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(100, 200)))
	return random_reply