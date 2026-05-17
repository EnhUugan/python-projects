while True:
    print("Welcome to Calculator")
    print(" ")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit!")
    print(" ")

    calc = int(input("Choose: "))
    print(" ")

    if calc == 5:
        print("OK!")
        break
    elif 1 <= calc <= 4:
        a = float(input("Pick a number: "))
        b = float(input("Pick a second number: "))
        print(" ")
    else:
        print("WRONG INPUT!")
        continue

    if calc == 1:
        print(f"{a} + {b} is {a + b}")
    elif calc == 2:
        print(f"{a} - {b} is {a - b}")
    elif calc == 3:
        print(f"{a} * {b} is {a * b}")
    elif calc == 4:
        if b == 0:
            print("Cannot divide by zero!")
        else:
            print(f"{a} / {b} is {a / b}")

        
