import hashlib
import hmac
import struct
import time
import os

TIME_STEP = 30
EPOCH = 0

"""
Generates a TOTP code from a key
@param key: key to generate the TOTP code
@return: TOTP code
"""
def ft_totp(key):
	key_bin = bytes.fromhex(key)
	current_time = int(time.time())
	time_counter = (current_time - EPOCH) // TIME_STEP
	time_counter_bin = struct.pack(">Q", time_counter) # '>Q' means big-endian unsigned long long (8 bytes)

	# Result in bytes
	hmac_result =  ft_hmac_sha1(key_bin, time_counter_bin)

	# Get last nibble
	offset = hmac_result[-1] & 0x0F

	# Gets 4 bytes from hmac after offset to form a 31 bit positive integer
	extended_code = (hmac_result[offset] & 0x7F) << 24 | \
					(hmac_result[offset + 1] & 0xFF) << 16 | \
					(hmac_result[offset + 2] & 0xFF) << 8 | \
					(hmac_result[offset + 3] & 0xFF)

	code = extended_code % 10**6

	# Zero-pad to ensure it has exactly 6 digits
	totp_str = f'{code:06d}'  # Format as a zero-padded 6-digit string

	return totp_str

def ft_hmac_sha1(key, message):
    # Block size of SHA-1 is 64 bytes
    block_size = 64
    
    # Ensure the key is of appropriate size
    if len(key) > block_size:
        key = hashlib.sha1(key).digest()  # Hash key if it's too long
    if len(key) < block_size:
        key = key + b'\x00' * (block_size - len(key))  # Pad key with zeros

    # Create inner and outer pads
    ipad = bytes((x ^ 0x36) for x in key)
    opad = bytes((x ^ 0x5C) for x in key)

    # Perform HMAC operation
    inner_hash = hashlib.sha1(ipad + message).digest()
    hmac_result = hashlib.sha1(opad + inner_hash).digest()

    return hmac_result
