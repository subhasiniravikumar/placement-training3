class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

account = BankAccount("Naveen", 1000)

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Display\n4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        account.deposit(int(input("Amount: ")))
    elif choice == "2":
        account.withdraw(int(input("Amount: ")))
    elif choice == "3":
        account.display()
    elif choice == "4":
        break
    else:
        print("Invalid option")
