import hashlib
import hmac
import struct
import time

TIME_STEP = 30
EPOCH = 0

def ft_totp(key):
	key_bin = bytes.fromhex(key)
	current_time = int(time.time())
	time_counter = (current_time - EPOCH) // TIME_STEP
	time_counter_bin = struct.pack(">Q", time_counter) # '>Q' means big-endian unsigned long long (8 bytes)

	# Create hmac-sha1 object
	hmac_sha1 = hmac.new(key_bin, time_counter_bin, hashlib.sha1)

	# Result in bytes
	hmac_result =  hmac_sha1.digest()

	# Result in hexadecimal
	hmac_hex = hmac_sha1.hexdigest()


	#print("HMAC-SHA1 (bytes): ", hmac_result)
	#print("HMAC-SHA1 (hex): ", hmac_hex)

	# Get last nibble
	offset = hmac_result[-1] & 0x0F

	#print("offset: ", offset)

	# Gets 4 bytes from hmac after offset to form a 31 bit positive integer
	extended_code = (hmac_result[offset] & 0x7F) << 24 | \
					(hmac_result[offset + 1] & 0xFF) << 16 | \
					(hmac_result[offset + 2] & 0xFF) << 8 | \
					(hmac_result[offset + 3] & 0xFF)

	#print("extended_code: ", extended_code)

	code = extended_code % 10**6

	# Zero-pad to ensure it has exactly 6 digits
	totp_str = f'{code:06d}'  # Format as a zero-padded 6-digit string

	return totp_str


