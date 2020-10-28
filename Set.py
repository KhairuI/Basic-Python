
'''
set1 = {4,3,4,5,2,'a',"Artless"} # duplicate value doesn't print ...
print(set1)
set1.add("al")
print(set1)

set2 = set([6,5, 4.5, 'D',"Jhon"])
print(set2)
print('D' in set2)

'''
a = {1,2,3,4,5}
b = set([4,5,6,7,8])

print(a | b) # Union
print(a & b) # intersection
print(a - b)

