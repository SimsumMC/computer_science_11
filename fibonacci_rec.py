global x


def fibonacci(n):
    global x
    x += 1
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    global x
    x = 0
    print(fibonacci(int(input("n="))))
    print("Aufrufe: " + str(x))
