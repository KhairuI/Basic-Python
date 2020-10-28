# Pattern

n = int(input("Enter A number: "))
for i in range(n+1):
    print((2*i-1) * "*")

# Another One
n2 = int(input("Enter A number: "))
for i in range(n2+1):
    print((n2-i) * " ",end="")
    print(i * "*")