import sys
import csv
import tabulate

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif sys.argv[1].find(".csv") == -1:
        print("Not a csv file")
        sys.exit(1)

    try:
        menu = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                menu.append(row)

        print(tabulate.tabulate(menu, headers="keys", tablefmt="grid"))

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()
