text = open("myFile.txt", "r")  # "r" = read , "w" = write , "r+" = read and write both .....
'''
print(text.readable())
print(text.read())
print(len("myFile.txt"))
'''

print(text.readlines()[1])

text.close()