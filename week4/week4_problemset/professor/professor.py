import random
import sys

def main():
    x = get_level()
    score = 0
    i = 10
    while i > 0:
        y = generate_integer(x)
        trys = 3
        while trys > 0:
            try:
                z = int(input(f"{y[0]} = "))
            except ValueError:
                z != y[1]
            if z != y[1]:
                print("EEE")
                trys = trys - 1
            elif z == y[1]:
                score = score + 1
                break
            if trys == 0:
                print(f"{y[0]} = {y[1]}")
                break
        i = i - 1
    print("Score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 3 and level !=2 and level != 1:
                raise ValueError
            return level
        except ValueError:
            None

def generate_integer(level):
    if level == 3:
        r3 = random.randint(100, 999)
        r33 = random.randint(100, 999)
        return f"{r3} + {r33}", r3 + r33
    elif level == 2:
        r2 = random.randint(10, 99)
        r22 = random.randint(10, 99)
        return f"{r2} + {r22}", r2 + r22
    elif level == 1:
        r1 = random.randint(0, 9)
        r11 = random.randint(0, 9)
        return f"{r1} + {r11}", r1 + r11

if __name__ == "__main__":
    main()
