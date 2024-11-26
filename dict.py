# Question 1
student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])
print(student["age"])
print(student["grade"])

# Question 2
fruits = {"apple": 2, "banana": 3, "orange": 1}

fruits["grape"] = 4

del fruits["banana"]

print(fruits)

# Question 3
person = {"name": "Alice", "city": "Wonderland"}

if "age" in person:
    print("'age' found.")
else:
    print("'age' not found.")

# Question 4 
numbers = list(range(1, 11))

print(numbers[:3])

print(numbers[-1])

# Question 5 
colors = ["red", "blue", "green"]

colors.append("yellow")
colors.remove("blue")

print(colors)

# Question 6
squares = [x**2 for x in range(1, 5)]
print(squares)

# Question 7 
fruit_tuple = ("apple", "banana", "cherry")
print(fruit_tuple[1])

# Question 8 
coordinates = (10, 20)

x, y = coordinates
print(x, y)

# Question 9
# colours = ("red", "green", "blue")

# colours.append("yellow")
# the tuple cannot be ammended due to '()' rather than '[]'

# Question 10
numbers = {1, 2, 3, 4}
numbers.add(5)
numbers.remove(2)
print(numbers)

# Question 11 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)

print(set3)
print(set4)

# Question 12
check = {5, 7, 9, 10, 12}
if 10 in check:
    print("'10' found.")
else:
    print("'10' not found.")

# Question 13
school = {
    "Alice": {"age": 14, "grade": "8th"},
    "Bob": {"age": 15, "grade": "9th"}
}

def get_grade(school, name):
    return school.get(name, {}).get("grade", "Student not found")

print(get_grade(school, "Alice")) 

# Question 14 
nums = [1, 2, 3, 4, 5]

sqr_num = {x: x**2 for x in nums}
print(sqr_num)

# Question 15 
inventory = {"apples": 5, "bananas": 3, "oranges": 2}

for fruit, quantity in inventory.items():
    print(f"We have {fruit}, {quantity}")


    
