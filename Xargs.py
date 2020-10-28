# Xargs.......
def add(x,y):
    sum = x+y
    return sum
def addition(*numbers):  #  it's work's like tuples
    s =0
    for i in numbers:
        s= s+i
    return s

print("The Sum is: ",add(10,2))

print("The sum is: ",addition(1,2,3,4,5,6))
print("The sum is: ",addition(1,29,3,4,34,91))