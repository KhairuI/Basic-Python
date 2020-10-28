
def user(id, name):
    print(id,name)
def student(**details):
    return details

user(id=10, name="Alex")

print("Student details: ",student(id=9838,name="Uzzal",CGPA= 3.75))
print("Student details: ",student(id=1234,name="Artless",CGPA= 3.75,phone="015173443"))