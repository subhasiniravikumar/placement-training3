def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = int(input("Enter n: "))
for val in fibonacci(n):
    print(val, end=" ")
