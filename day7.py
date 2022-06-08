import re

pat_affectation = re.compile(r'(\d+) -> ([a-z]+)')
pat_binary_op = re.compile(r'(\d+) (AND|OR|RSHIFT|LSHIFT) (\d+) -> ([a-z]+)')
pat_unary_op = re.compile(r'NOT (\d+) -> ([a-z]+)')

def find_simplest_instruction(line):
	m = pat_affectation.fullmatch(line)
	if m:
		return True, m.group(2), m.group(1)
	return False, '', ''

def find_computable_op(line):
	if True in find_simplest_instruction(line):
		return find_simplest_instruction(line)
	m = pat_unary_op.fullmatch(line)
	if m:
		return True, m.group(2), str(65535 - int(m.group(1)))
	m = pat_binary_op.fullmatch(line)
	if not m:
		return False, '', ''
	operandl = int(m.group(1))
	operator = m.group(2)
	operandr = int(m.group(3))
	if operator == 'AND':
		val = operandl & operandr
	elif operator == 'OR':
		val = operandl | operandr
	elif operator == 'LSHIFT':
		val = operandl << operandr
	else: # operator == 'RSHIFT'
		val = operandl >> operandr
	return True, m.group(4), str(val)

def replace_value_multiple(line, known_values):
	new_line = ''
	string = line.split(' ')
	for i, token in enumerate(string):
		if token in known_values:
			string[i] = known_values[token]
			new_line = ' '.join(string)
	return new_line
 

with open('inputDay7.txt', 'r') as f:
	circuit_lines = f.read().split('\n')

# Trouver les premiers instructions complete: b, c
known_values = {}
for line in circuit_lines:
	res, var, val = find_simplest_instruction(line)
	if res:
		known_values[var] = val
known_values['b'] = '956'


found_count = 0
while ('a' not in known_values) and len(known_values) != found_count:
	found_count = len(known_values)
	for line in circuit_lines:
		new_line = replace_value_multiple(line, known_values)
		if new_line:
			res, var, val = find_computable_op(new_line)
			if res:
				known_values[var] = val
	#print(len(known_values), known_values)

print(known_values['a'])

