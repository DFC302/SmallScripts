#!/usr/bin/env python3

import enchant
import sys
import argparse
import random
from itertools import product
from string import ascii_lowercase

def options():
	parser = argparse.ArgumentParser()

	parser.add_argument(
		"--reduce", "-r",
		help="Used with generate-words flag, used to produce all words of a given length and reduce down to two words.",
		action="store_true",
	)

	parser.add_argument(
		"--letters", "-L",
		help="Used specific letters over entire alphabet.",
		action="store",
		type=str,
	)

	parser.add_argument(
		"--out", "-o",
		help="Write results to file.",
		action="store",
	)

	parser.add_argument(
		"--length", "-l",
		help="Specify length of words",
		action="store",
		type=int,
	)

	parser.add_argument(
		"--dict", "-d",
		help="Choose dictionary.",
		action="store",
		type=str,
	)

	parser.add_argument(
		"--check-dict", "-cd",
		help="Check if dictionary exists to be used.",
		action="store",
	)

	parser.add_argument(
		"--verbose", "-v",
		help="Turn on verbose mode.",
		action="store_true",
	)

	parser.add_argument(
		"--version", "-V",
		help="Print version and author information.",
		action="store_true",
	)

	# if not arguments are given, print usage message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	args = parser.parse_args()
	return args

def check_if_dict_exists():
	if options().check_dict:
		isDict = options().check_dict
		checkDict = enchant.dict_exists(isDict)

		if checkDict == True:
			print("Dictionary exists")
			print(f"Using {isDict} dictionary as default.")
			dictionary = enchant.Dict(isDict)
			return dictionary

		elif checkDict == False:
			print("Dictionary does not exist")
			print("Using default dictionary \"en-US\"")
			dictionary = enchant.Dict(isDict)
			return dictionary

	elif not options().check_dict:
		dictionary = enchant.Dict("en-US")
		return dictionary

def all_words_given_length():
	dictionary = check_if_dict_exists()

	if options().length:
		length = options().length

	elif not options().length:
		length = 5

	if options().letters:
		letters = options().letters

		if len(letters) < length:
			if options().verbose:
				print("Letters are less than chosen length.")
				print("Adding random letters to poportioned size.\n")

			i = len(letters)
			while i < length:
				letters = f"{random.choice(ascii_lowercase)}{letters}"
				i+=1

			print("Debug letters:", letters)

	elif not options().letters:
		letters = ascii_lowercase

	possWords = ["".join(v) for v in product(letters, repeat=length)]

	for word in possWords:
		checkWord = dictionary.check(word)

		if checkWord == True:
			print(word)

		elif checkWord == False and options().verbose:
			print(word)

def all_words_given_length_reduced():
	dictionary = check_if_dict_exists()

	if options().length:
		length = options().length

	elif not options().length:
		length = 5

	i = length

	if options().letters:
		letters = options().letters

		if len(letters) < length:
			if options().verbose:
				print("Letters are less than chosen length.")
				print("Adding random letters to poportioned size.\n")

			i = len(letters)
			while i < length:
				letters = f"{random.choice(ascii_lowercase)}{letters}"
				i+=1

			print("Debug letters:", letters)

	elif not options().letters:
		letters = ascii_lowercase

	while i >= 2:
		possWords = [''.join(i) for i in product(letters, repeat = i)]
		
		for word in possWords:
			checkWord = dictionary.check(word)

			if checkWord == True:
				print(word)

			elif checkWord == False and options().verbose:
				print(word)

		i-=1

def main():
	if options().reduce:
		all_words_given_length_reduced()

	if not options().reduce:
		all_words_given_length()

if __name__ == "__main__":
	main()
