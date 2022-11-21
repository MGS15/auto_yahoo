import random
import string

def random_wait_time(min: int, max: int):
	return random.randint(min, max)

def generate_relpy_message():
	random_reply = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=random.randint(100, 200)))
	return random_reply