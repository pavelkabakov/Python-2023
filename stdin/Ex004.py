file_in = open("input_1.txt", encoding="UTF-8")
for line in file_in:
    print(line.rstrip("\n"))
file_in.close()