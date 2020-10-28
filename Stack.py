#  Stack ->  LIFO - Last in First Out .....
print("Stack Example........")
code = ["Python"]

code.append("Ruby")
code.append(["Kotlin","Prolog"])
print(code)
code.pop()
print(code)
code.append("Java")
print(code)
print("Top code is ",code[-1])

code.pop()
print(code)
print("Top code is ",code[-1])

