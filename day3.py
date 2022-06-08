def count_houses(liste):

	position = [0,0]
	houses = set()
	houses.add(tuple(position))

	for caracter in liste:
		if caracter == "^":
			position[1] = position[1] + 1
		elif caracter == "v":
			position[1] = position[1] - 1
		elif caracter == ">":
			position[0] = position[0] + 1
		elif caracter == "<":
			position[0] = position[0] - 1

		houses.add(tuple(position))

	print(len(houses))
	return houses

liste_complete = open("inputDay3.txt").read()
liste_robo = liste_complete[1::2]
liste_santa = liste_complete[0::2]

houses_robo_santa = set()

houses_robo_santa = count_houses(liste_robo).union(count_houses(liste_santa))
print(len(houses_robo_santa))
f = open("inputDay3.txt", "r")
print(f.readline())