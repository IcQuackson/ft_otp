from otp import ft_totp
import argparse
import sys
from key_manager import save_key

def parse_args():
	parser = argparse.ArgumentParser(description="ft_otp arguments")
	parser.add_argument('-g', help='Flag to store given hexadecimal key', action='store')
	parser.add_argument('-k', help='Flag to generate code with given key', action='store')
	args = parser.parse_args()

	if args.g and args.k:
		raise ValueError("Error. Both -g and -k flag cannot be set at the same time!")
	if not args.g and not args.k:
		raise ValueError("Error. You must set either -g or -k flag!")
	
	return args


if __name__ == "__main__":

	try:
		args = parse_args()

		if args.g:
			save_key(args.g)
			pass
		elif args.k:
			#generate code with key
			print("key to generate code: ", args.k)
			pass

	except Exception as e:
		print(e)
		sys.exit(1)
