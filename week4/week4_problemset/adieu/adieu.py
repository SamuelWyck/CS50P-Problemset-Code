import inflect
p = inflect.engine()

def main():
    allname = []
    try:
        while True:
            name = input("Name: ")
            allname.append(name)

    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(allname))

if __name__ == "__main__":
    main()


