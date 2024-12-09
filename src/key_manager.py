import os
import sys
from utils import is_file_valid, create_or_replace_file_with_content
from hotp_generator import ft_totp

MINIMUM_KEY_LEN = 32
OUTPUT_KEY_NAME = "ft_otp.key"
ALLOWED_KEY_TO_SAVE_FILE_EXTENSIONS = ('.txt')
ALLOWED_KEY_TO_GENERATE_FILE_EXTENSIONS = ('.key')
SAVE = 'SAVE'
GENERATE = 'GENERATE'

def is_key_valid(key):

	if len(key) < MINIMUM_KEY_LEN:
		return False, f'Key must have at least 64 numbers'

	try:
		int(key, 16)
	except Exception as e:
		return False, f'Key is not an hexadecimal number'

	return True, None

def extract_key(key_path, mode):
	allowed_file_extensions = ()

	if mode == SAVE:
		allowed_file_extensions = ALLOWED_KEY_TO_SAVE_FILE_EXTENSIONS
	if mode ==  GENERATE:
		allowed_file_extensions = ALLOWED_KEY_TO_GENERATE_FILE_EXTENSIONS

	file_valid, error = is_file_valid(key_path, allowed_file_extensions)

	if not file_valid:
		raise ValueError(error)
	
	key = ''
	with open(key_path, 'r') as file:
		key = file.readline().strip()
	
	key_valid, error = is_key_valid(key)

	if not key_valid:
		raise ValueError(error)

	return key

def save_key(key_path):

	key = extract_key(key_path, SAVE)
	
	create_or_replace_file_with_content(OUTPUT_KEY_NAME, key)

	print(f'Key saved in {OUTPUT_KEY_NAME}')


def generate_code_from_key(key_path):
	key = extract_key(key_path, GENERATE)
	code = ft_totp(key)
	print(code)

