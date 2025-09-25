# Appending to Text Files 

# (1) APPEND ONE LINE
file = open("example.txt", "a")
file.write("Appended line 1.\n")
file.close()

# (2) APPEND MULTIPLE LINES
file = open("example.txt", "a")
file.writelines([
    "Appended line 2.\n",
    "Appended line 3.\n"
])
file.close()
