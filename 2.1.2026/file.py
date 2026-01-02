def add_student():
    with open("students.txt", "a") as file:
        roll = input("Roll No: ")
        name = input("Name: ")
        marks = input("Marks: ")
        file.write(f"{roll},{name},{marks}\n")
    print("Student added successfully")

def view_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    except FileNotFoundError:
        print("No records found")

while True:
    print("\n1.Add Student\n2.View Students\n3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
