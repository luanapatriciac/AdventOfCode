def basement (chaine):
	countMontant = countDecendant = 0
	
	for car in chaine:
		if car == '(':
			countMontant += 1
		else:
			countDecendant += 1

		if countDecendant == countMontant + 1:
			return countDecendant + countMontant

with open ("input.txt",'r') as f: 
	chaine = f.read()

print(basement(chaine))