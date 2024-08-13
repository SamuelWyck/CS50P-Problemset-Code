import sys
import csv

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    try:
        before = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["last"], row["first"] = row["name"].replace(" ","").split(",")
                del row["name"]
                before.append(row)

        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            n = 0
            while True:
                try:
                    writer.writerow(before[n])
                    n = n + 1
                except IndexError:
                    break

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()
