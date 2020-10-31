# map and filter function......

def cube(a):
    return pow(a, 3)

numbers = [ 1,2,3,4,5 ]
result = list(map(cube, numbers))
print(result)

# Filter
numbers2 = [1, 2, 3, 4, 5, 6]
value = list(filter(lambda x: x % 2 == 1, numbers2))
print(value)

# List Comprehensions

v = [cube(b) for b in numbers]   # map function minimize
print(v)

r = [c for c in numbers2 if c % 2 == 1]   # Filter function minimize
print(r)

