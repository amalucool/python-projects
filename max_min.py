numbers = [1, 5, -1, 6, 12, -9, 100, 56, -12, -2345, 23, 123, 567, 56, -90, 34, 78, -123, 1678]
max_num = numbers[0]
min_num = numbers[0]
count = 0
all_numbers = 0

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num 
    count += 1
    all_numbers += num


print("Maximum",max_num)
print("Minimum", min_num)
print("Total numbers", count)
print("The sum is", all_numbers)


