# Reading Text Files (2025)

# (1) READ ENTIRE FILE
file = open("example.txt", "r")
content = file.read()
print("Full content:\n", content)
file.close()

# (2) READ LINE BY LINE
file = open("example.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# (3) READ FIRST LINE
file = open("example.txt", "r")
first_line = file.readline()
print("First line:", first_line.strip())
file.close()
