import re

def parse_line(line):
	m = re.fullmatch(r'(\w+) to (\w+) = (\d+)', line.strip())
	if not m:
		raise ValueError(f'Unable to parse line "{line}"')
	return m.group(1), m.group(2), int(m.group(3))


with open('inputDay9.txt', 'r') as file:
	greatest_distance = 0
	lines = []

	for line in file:
		lines.append(line)


total = 0
count = 0
last_destination = ''

while len(lines) != 0:
	greatest_distance = 0

	for line in lines:
		if last_destination in line:
			orig, dest, dist = parse_line(line)
			if dist > greatest_distance:
				greatest_distance = dist
				origin = dest
				destination = orig
	total += greatest_distance

	if count != 0 and origin != last_destination:
		destination = origin
		origin = last_destination	
	print(origin,destination,total, greatest_distance)

	connections_with_origin = [l for l in lines if origin in l]	

	for segment in connections_with_origin:	
		lines.remove(segment)

	last_destination = destination

	count += 1

print(f"{total=}")
	
		
		