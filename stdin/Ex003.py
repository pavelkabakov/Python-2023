from sys import stdin

lines = []
for line in stdin:
    # lines.append(line)
    if line == 'q':
        break
    else:
        print(line)

