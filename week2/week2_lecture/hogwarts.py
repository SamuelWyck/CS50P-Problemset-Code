#students = ["Hermione", "Harry", "Ron"]

#for i in range(len(students)):
 #   print(i + 1, students[i])

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronous": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for i in students:
    print(i["name"], i["house"], i["patronous"], sep=", ")

