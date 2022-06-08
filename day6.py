def create_grid (dimension):
	grid = list()
	for _ in range(dimension):
		grid.append([0] * dimension)
	return grid		

def conversion_line(line):
	command = line.split(' ')
	if 'toggle' in line:
		a,b = command[1].split(',')
	else:
		a,b = command[2].split(',')
	c,d = command[-1].split(',')
	begin_c = int(a)
	begin_l = int(b)
	end_c = int(c)
	end_l = int(d)

	return begin_c,begin_l,end_c,end_l

def turn_lights(grid,line,mode):
	begin_c,begin_l,end_c,end_l = conversion_line(line)	

	for l in range(begin_l, end_l + 1):
		for c in range(begin_c, end_c + 1):
			grid[l][c] = mode


def toggle_lights(grid,line):
	begin_c,begin_l,end_c,end_l = conversion_line(line)

	for l in range(begin_l, end_l + 1):
		for c in range(begin_c, end_c + 1):
			if grid[l][c] == 1:
				grid[l][c] = 0
			else:
				grid[l][c] = 1		

def turn_lights_on_real(grid,line):
	begin_c,begin_l,end_c,end_l = conversion_line(line)	
	brightness = 0

	for l in range(begin_l, end_l + 1):
		for c in range(begin_c, end_c + 1):
			grid[l][c] += 1
			brightness += 1

	return brightness

def turn_lights_off_real(grid,line,brightness):
	begin_c,begin_l,end_c,end_l = conversion_line(line)	

	for l in range(begin_l, end_l + 1):
		for c in range(begin_c, end_c + 1):
			if grid[l][c] > 0:
				grid[l][c] -= 1
				brightness -= 1

	return brightness
					

def toggle_lights_real(grid,line):
	begin_c,begin_l,end_c,end_l = conversion_line(line)
	brightness = 0

	for l in range(begin_l, end_l + 1):
		for c in range(begin_c, end_c + 1):
			grid[l][c] += 2	
			brightness += 2

	return brightness 


with open('inputDay6.txt','r') as f:
	grid = create_grid(1000)
	brightness = 0


	for line in f:
		if 'turn on' in line:
			brightness += turn_lights_on_real(grid,line)
		if 'turn off' in line:
			brightness = turn_lights_off_real(grid,line,brightness)
		if 'toggle' in line:
			brightness += toggle_lights_real(grid,line)
		print(line,brightness)
	
	






	