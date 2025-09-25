# Working with JSON Files
import json

# (1) CREATE JSON FILE AND WRITE DATA
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

file = open("data.json", "w")
json.dump(data, file)
file.close()

# (2) READ JSON FILE
file = open("data.json", "r")
content = json.load(file)
print("Content:", content)
file.close()

# (3) APPEND-LIKE: UPDATE AND REWRITE JSON
file = open("data.json", "r")
content = json.load(file)
file.close()

content["email"] = "alice@example.com"

file = open("data.json", "w")
json.dump(content, file)
file.close()
