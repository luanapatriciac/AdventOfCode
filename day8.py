import re

def count_caracters_code(line):
	pat_hexa = re.compile(r'\\x[0-9a-f]{2}')
	counthexa = len(pat_hexa.findall(line))
	return line.count('\\\\') + line.count('\\\"') + 3*counthexa

def increase_count_caracters_code(line):
	pat_hexa = re.compile(r'\\x[0-9a-f]{2}')
	count_backslash = len(re.findall(r'\\', line))
	count_quotes = len(re.findall(r'\"',line))
	return count_quotes + count_backslash


with open('inputDay8.txt', 'r') as file:
	result = 0
	new_string = 0
	for line in file:
		result += count_caracters_code(line[1:-2]) + 2
		new_string += increase_count_caracters_code(line) + 2

print(result)
print(new_string)




