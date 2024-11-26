def add(a, b):
    return a + b 
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def calculator():
    print("Welcome to Amals Calculator")
    print("select and operation")
    print("a. add")
    print("b. subtract")
    print("c. multiply")
    print("d. divide")

    choice = input("Enter choice (a, b, c, d): ")
    if choice in ['a', 'b', 'c', 'd']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == 'a':
                print("Result:", add(num1, num2))
            elif choice == 'b':
                    print("Result:", subtract(num1, num2))
            elif choice == 'c':
                print("Result:", multiply(num1, num2))
            elif choice == 'd':
              print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input that is not defiined")
    else:
        print("Invalid choice!")

calculator()
              

            







    