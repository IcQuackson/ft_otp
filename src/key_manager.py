import os
from utils import is_file_valid, create_or_replace_file_with_content, create_qr_code
from otp_generator import ft_totp

MINIMUM_KEY_LEN = 32
OUTPUT_KEY_NAME = "ft_otp.key"
ALLOWED_KEY_TO_SAVE_FILE_EXTENSIONS = ('.txt')
ALLOWED_KEY_TO_GENERATE_FILE_EXTENSIONS = ('.key')
SAVE = 'SAVE'
GENERATE = 'GENERATE'

"""
Checks if the key is valid
@param key: key to be validated
@return: tuple with a boolean and an error message
"""
def is_key_valid(key):

	if len(key) < MINIMUM_KEY_LEN:
		return False, f'Key must have at least 64 numbers'

	try:
		int(key, 16)
	except Exception as e:
		return False, f'Key is not an hexadecimal number'

	return True, None

"""
Extracts the key from a file
@param key_path: path to the file containing the key
@param mode: mode to differentiate between the allowed file extensions for saving and generating
@return: key extracted from the file
"""
def extract_key(key_path, mode):
	allowed_file_extensions = ()

	# Mode exists to differentiate between the allowed file extensions for saving and generating
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

"""
Saves the key in a file and generates a QR code
@param key_path: path to the file containing the key
@param key: key to be saved
"""
def save_key(key_path, key):
	if not key:
		key = extract_key(key_path, SAVE)
	create_or_replace_file_with_content(OUTPUT_KEY_NAME, key)
	create_qr_code(key)

	print(f'Key saved in {OUTPUT_KEY_NAME}')

"""
Generates a code from a key
@param key_path: path to the file containing the key
"""
def generate_code_from_key(key_path):
	key = extract_key(key_path, GENERATE)
	code = ft_totp(key)
	print(code)

"""
Generates a random key
@return: random key
"""
def generate_random_key():
	return os.urandom(32).hex()

"""
Generates a QR code with seed generation
"""
def generate_qr_code_with_seed_generation():
	save_key(None, generate_random_key())
	