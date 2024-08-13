#name = input("what's your name? ")


#with open("names.txt", "a") as file:
  #  file.write(f"{name}\n")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


#writing to a csv file
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}")

