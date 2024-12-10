import os 
import hashlib

HASH_ITERATIONS = 100_000

"""
Encrypts or decrypts data using XOR
@param data: data to be encrypted or decrypted
@param key: key to be used in the encryption or decryption
@return: encrypted or decrypted data
"""
def xor_encrypt_decrypt(data, key):
	return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

"""
Derives a key from a password and a salt
@param password: password to derive the key
@param salt: salt to derive the key
@param length: length of the key
@return: derived key
"""
def derive_key(password, salt, length=32):
	return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, HASH_ITERATIONS, dklen=length)

"""
Saves an encrypted secret to a file
@param secret: secret to be encrypted and saved
@param password: password to encrypt the secret
@param filename: name of the file to save the encrypted secret
"""
def save_encrypted_secret(secret, password, filename):
	salt = os.urandom(16)
	key = derive_key(password, salt)
	encrypted_data = xor_encrypt_decrypt(secret.encode(), key)
	with open(filename, "wb") as f:
		f.write(salt + encrypted_data)

"""
Loads an encrypted secret from a file
@param password: password to decrypt the secret
@param filename: name of the file to load the encrypted secret
@return: decrypted secret
"""
def load_encrypted_secret(password, filename):
	with open(filename, "rb") as file:
		content = file.read()
	
	salt = content[:16]
	encrypted_data = content[16:]
	key = derive_key(password, salt)
	decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
	return decrypted_data