import argparse
import sys
from key_manager import save_key, generate_code_from_key, generate_qr_code_with_seed_generation

def parse_args():
	parser = argparse.ArgumentParser(description="ft_otp arguments")
	parser.add_argument('-g', help='Flag to store given hexadecimal key', action='store')
	parser.add_argument('-k', help='Flag to generate code with given key', action='store')
	parser.add_argument('-s', help='Flag to generate qr code with seed generation', action='store_true')
	args = parser.parse_args()

	if sum(bool(flag) for flag in [args.g, args.k, args.s]) > 1:
		raise ValueError("Error. Cannot have more than one flag set at the same time!")
	if not args.g and not args.k and not args.s:
		raise ValueError("Error. You must set either -g, -k or -s flag!")
	
	return args


if __name__ == "__main__":

	try:
		args = parse_args()

		if args.g:
			save_key(args.g, None)
		elif args.k:
			generate_code_from_key(args.k)
		elif args.s:
			generate_qr_code_with_seed_generation()

	except Exception as e:
		print(e)
		sys.exit(1)
