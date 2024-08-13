from datetime import date
import inflect
import sys
p = inflect.engine()


def main():
    bday = input("Date of Birth: ")
    print(age(bday))

def age(bday):
    today = date.today()
    try:
        bday = date.fromisoformat(bday)
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    age = today - bday
    age = age * 1440
    age = str(age).split(" ")
    age = int(age[0])
    return f"{p.number_to_words(age, andword="").capitalize()} minutes"



if __name__ == "__main__":
    main()
