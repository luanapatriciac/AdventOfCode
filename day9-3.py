import re


def parse_line(line):
    m = re.fullmatch(r'(\w+) to (\w+) = (\d+)', line.strip())
    if not m:
        raise ValueError(f'Unable to parse line "{line}"')
    return m.group(1), m.group(2), int(m.group(3))


with open('inputDay9.txt', 'r') as file:
    greatest_distance = 100000
    lines = []

    for line in file:
        orig, dest, dist = parse_line(line)
        if dist < greatest_distance:
            greatest_distance = dist
            origin = orig
            origin2 = dest
        lines.append(line)

total = 0
while len(lines) != 0:
    smallest_distance = greatest_distance

    connections_with_origin = [l for l in lines if origin in l]

    for l in connections_with_origin:
        orig, dest, dist = parse_line(l)
        if dist > smallest_distance:
            smallest_distance = dist
            new_destination = dest if dest != origin else orig
    origin = new_destination

    for segment in connections_with_origin:
        lines.remove(segment)

    total += smallest_distance

print(f"{total=}")
