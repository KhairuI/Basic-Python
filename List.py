
# List
course = ["Artless", "Uzzal", "Alex", "Jhon", "Alice", "Anik"]



'''
print(course)
print(course[0])
print(course[2:])

# Check a item in list

print("Alex" in course)
print("Alem" in course)
print("Alem" not in course)

print(len(course))
# add at last
course.append("Anika")
print(course)
'''
course.insert(2,"Boobs")
print(course)
course.remove("Artless")
print(course)

a = [12,4,3,7,3,80,3]
a.sort()
print(a)
a.reverse()
print(a)

b = a.copy()
print(b)
# see item position
print(b.index(3))

# a item how many time have
print(b.count(3))

# Range
r1 = list(range(8))
print(r1)

r2 = list(range(5, 12))
print(r2)

r3 = list(range(5, 20, 2))
print(r3)

