library = {}

while True:
    print("\n1.Add Book 2.Borrow Book 3.Display Books 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book name: ")
        library[book] = library.get(book, 0) + 1

    elif ch == 2:
        book = input("Enter book name: ")
        if library.get(book, 0) > 0:
            library[book] -= 1
            print("Book Issued")
        else:
            print("Book Not Available")

    elif ch == 3:
        print("Available Books:", library)

    elif ch == 4:
        break
