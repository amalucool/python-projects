# question NO.1
a= [3, 1, 4, 1, 5, 9, 2, 6, 5]
print( sorted(a) )
a = list(reversed( sorted(a)))
print(a)
             
# question NO.2
b= [1, 2, 2, 3, 4, 4, 5]
b = list(set(b))
print(b)

# question NO.3
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in c:
    print(" ".join(map(str, row)))

# question NO.4
d = [10, 15, 20, 25, 30]
new_list = [num for num in d if num % 5 == 0 and num > 15]
print(new_list)

# question NO.5
e = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

e = sum(e, [])
 
print(e)