import os
import sys
import qrcode
import base64

"""
Checks if a file is valid
@param file: file to be validated
@param allowed_extensions: allowed file extensions
@return: tuple with a boolean and an error message
"""
def is_file_valid(file, allowed_extensions):
    if not os.path.isfile(file):
        return False, f'Error: File {file} does not exist!'
    
    if not os.access(file, os.R_OK):
        return False, f'Error: File {file} does not have read permission'
    
    if not file.lower().endswith(allowed_extensions):
        return False, f'Error: allowed extensions: {allowed_extensions}'
    
    return True, None

"""
Creates or replaces a file with content
@param filename: name of the file to be created or replaced
@param content: content to be written in the file
"""
def create_or_replace_file_with_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

"""
Creates a QR code
@param data: data to be encoded in the QR code
"""
def create_qr_code(data):

	byte_secret_key = bytes.fromhex(data)
	base32_secret_key = base64.b32encode(byte_secret_key).decode('utf-8').rstrip('=')

	account_name = "ft_otp:ft_otp@42.com"
	issuer = "ft_otp"
	otp_auth_url = f"otpauth://totp/{account_name}?secret={base32_secret_key}&issuer={issuer}"

	qr = qrcode.QRCode(
		version=1,  # Controls the size of the QR code (1 is the smallest)
		error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
		box_size=10,
		border=4,
	)

	# Add data to the QR code
	qr.add_data(otp_auth_url)
	qr.make(fit=True)

	# Generate the QR code image
	qr_image = qr.make_image(fill_color="black", back_color="white")
	qr_image.save("qrcode.png")

	print("QR Code saved in qrcode.png")