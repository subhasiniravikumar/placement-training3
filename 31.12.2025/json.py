import json

data = {
    "name": "Naveen",
    "dept": "AIML",
    "year": 3
}

with open("student.json", "w") as f:
    json.dump(data, f)

with open("student.json", "r") as f:
    content = json.load(f)
    print("Student Data:", content)
