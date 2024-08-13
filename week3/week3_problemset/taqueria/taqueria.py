def main():
    d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    try:
        while True:
            item = input("Item: ").title()
            if item in d:
                print(f"${d[item]:.2f}")
                break
            elif item not in d:
                None
        while True:
            if item in d:
                try:
                    d[item] = d[item] + y
                    print(f"${d[item]:.2f}")
                except NameError:
                    pass
                y = d[item]
                item = input("Item: ").title()
            elif item not in d:
                item = input("Item: ").title()
    except EOFError:
        print()
        exit()

main()
