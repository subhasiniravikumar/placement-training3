def add_student():
    with open("students.txt", "a") as f:
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        f.write(f"{roll},{name}\n")

def display_students():
    with open("students.txt", "r") as f:
        for line in f:
            roll, name = line.strip().split(",")
            print("Roll:", roll, "Name:", name)

while True:
    print("\n1.Add Student 2.Display Students 3.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        add_student()
    elif ch == 2:
        display_students()
    elif ch == 3:
        break
