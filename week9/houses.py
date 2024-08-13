students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]

#sets are like lists but they get rid of duplicates
houses = set()

for student in students:
   houses.add(student["house"])

for house in sorted(houses):
    print(house)
