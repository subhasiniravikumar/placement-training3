class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print("Amount Deposited")

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

acc = BankAccount("Naveen", 5000)

while True:
    print("\n1.Deposit 2.Withdraw 3.Display 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        acc.deposit(int(input("Enter amount: ")))
    elif ch == 2:
        acc.withdraw(int(input("Enter amount: ")))
    elif ch == 3:
        acc.display()
    elif ch == 4:
        break
