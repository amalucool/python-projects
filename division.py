def division_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"The answer of {num1} by {num2} is {result}.")
    finally:
        print("Thank for using calc")
division_calculator()
