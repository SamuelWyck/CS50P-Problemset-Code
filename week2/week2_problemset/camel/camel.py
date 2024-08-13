def main():
    v = input("camelCase: ")
    print("snake_case: ", end="")
    for c in v:
        if c.islower() == False:
            print("_", end="")
        print(c.lower(), end="")
    print()
main()

