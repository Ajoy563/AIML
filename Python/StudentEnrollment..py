info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]
s = set()
for course in info:
    s.add(course[1])
print(s)

for name, course in info:
    if(course == "English") :
        print(name, end = " ")

print()
student = dict()
for name, course in info:
    if(student.get(name) == None):
        student.update({name : set()})
        student[name].add(course)
    else:
        student[name].add(course)
print(student)