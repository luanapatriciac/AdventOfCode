def dimensions (line):
	h,l,w = line.split("x")
	h = int(h)
	l = int(l)
	w = int(w)
	return (h,l,w)


def surface (line):
	h,l,w = dimensions(line)

	if h >= l and h >= w:
		slack = l * w
	elif l >= h and l >= w:
		slack = h * w
	else:
		slack = l * h

	surfaceArea = 2*l*w + 2*w*h + 2*h*l

	return surfaceArea + slack


def ribbon(line):
	h,l,w = dimensions(line)

	if h >= l and h >= w:
		wrap = 2*l + 2*w
	elif l >= h and l >= w:
		wrap = 2*h + 2*w
	else:
		wrap = 2*l + 2*h

	bow = l*h*w

	return wrap + bow


with open ("inputDay2.txt",'r') as f: 
	totalArea = 0
	totalLength = 0
	for line in f:
		totalArea += surface(line)
		totalLength += ribbon(line)

print(totalArea)
print(totalLength)


