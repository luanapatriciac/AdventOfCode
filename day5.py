def forbiden_pairs(line):	
	return not ('ab' in line or 'cd' in line or 'pq' in line or 'xy' in line)

def enough_vowels(line, num_min_vowels=3):
	count_vowels = 0
	for caracter in line:			
		if caracter in 'aeiou':
			count_vowels = count_vowels + 1
	return count_vowels >= num_min_vowels

def duplicate_caracter(line):
	caracter_before = ""
	for caracter in line:
		pair_letters = caracter_before + caracter	
		if caracter == caracter_before:
			return True	
		caracter_before = caracter
		
	return False

def nice_string(line):
	return forbiden_pairs(line) and enough_vowels(line) and duplicate_caracter(line)
			

def one_letter_between(line):
	for i in range(len(line)-2):

		if line[i] == line[i+2]:
			return True		

	return False

def duplicate_pairs(line):
	for i in range(len(line)-1):
		pair_letters = line[i:i+2]
		
		if line.count(pair_letters) > 1:
			return True

	return False

def new_nice_string(line):
	return one_letter_between(line) and duplicate_pairs(line)

with open ("inputDay5.txt",'r') as f:
	all_nice_string = [line for line in f if new_nice_string(line)]
	print(len(all_nice_string))

with open('result.txt', 'w') as file:
	file.write(''.join(all_nice_string))


				

		


		



