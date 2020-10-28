
digit = 0
word = 0
letter = 0
n = input("Enter a number text: ")
'''
list = n.split()  # splite this string based on space

for i in list:
    print(i)
'''
for i in n:
    i.lower()
    if i >= 'a' and i <= 'z':
        letter = letter + 1
    elif i>= '0' and i<= '9':
        digit= digit+1
    elif i == ' ':
        word= word+1

print("Digit: ", digit)
print("Letter: ", letter)
print("Word: ", word)


