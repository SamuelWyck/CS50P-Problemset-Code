import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                level = int(input("Level: "))
            y = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess == y:
                        print("Just right!")
                        sys.exit(0)
                    elif guess > y:
                        print("Too large!")
                    elif guess < y:
                        print("Too small!")
                except ValueError:
                    None


        except ValueError:
            None


if __name__ == "__main__":
    main()



