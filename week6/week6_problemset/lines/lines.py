import csv
import sys

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif sys.argv[1].find(".py") == -1:
        print("Not a python file")
        sys.exit(1)

    lines = []
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") == True or line == "":
                    None
                else:
                    lines.append(line)

        print(len(lines))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
