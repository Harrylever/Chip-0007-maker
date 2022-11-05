import random

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def randomize():
	value_string = []
	for i in range(0, 4):
		value_string.append(random.choice(small_letters))
		value_string.append(random.choice(capital_letters))
		value_string.append(str(random.choice(all_numbers)))
		value_string.append(str(random.choice(all_numbers)))
	
	random.shuffle(value_string)
	value_str = ""

	for char in value_string:
		value_str += char

	return value_str
