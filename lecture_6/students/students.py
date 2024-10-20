# with open("students.csv") as file:
#     for line in file:
#         name , location = line.rstrip().split(",")
#         print(f"{name} lives in {location}")


students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


"""
def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
"""

# abouve code equivalent to below code

for student in sorted(students, key=lambda student: student["name"]): # reverse=True for descending order
    print(f"{student['name']} is in {student['house']}")
