# Question 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

sorted_numbers = sorted(numbers)
reversed_sorted_numbers = sorted_numbers[::-1]

print(sorted_numbers)
print(reversed_sorted_numbers)

# Question 2 
def remove(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove(nums))

# Question 3 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    print(" ".join(map(str, row)))

# Question 4 
numbers = [10, 15, 20, 25, 30]

result = [num for num in numbers if num > 15 and num % 5 == 0]
print(result)

# Question 5 
def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(flatten(nested_list))