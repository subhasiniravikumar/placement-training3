class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Not eligible to vote")
    print("Eligible to vote")
except AgeError as e:
    print(e)
