add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "0 cannot be divided"

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

print(f"The result of addition is: {add(x, y)}")
print(f"The result of subtraction is: {subtract(x, y)}")
print(f"The result of multiplication is: {multiply(x, y)}")
print(f"The result of division is: {divide(x, y)}")

