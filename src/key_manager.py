import os
import sys
from utils import is_file_valid, create_or_replace_file_with_content

MINIMUM_KEY_LEN = 32
OUTPUT_KEY_NAME = "ft_otp.key"

def is_key_valid(key):

	if len(key) < MINIMUM_KEY_LEN:
		return False, f'Key must have at least 64 numbers'

	try:
		int(key, 16)
	except Exception as e:
		return False, f'Key is not an hexadecimal number'

	return True, None


def save_key(key_path):

	file_valid, error = is_file_valid(key_path)

	if not file_valid:
		raise ValueError(error)
	
	key = ''
	with open(key_path, 'r') as file:
		key = file.readline().strip()
	
	key_valid, error = is_key_valid(key)

	if not key_valid:
		raise ValueError(error)
	
	create_or_replace_file_with_content(OUTPUT_KEY_NAME, key)

	print(f'Key saved in {OUTPUT_KEY_NAME}')
	
