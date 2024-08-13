def main():
    x = input("Greeting: ").lower().lstrip()
    y = x.find("hello")
    if y == 0:
        print("$0")
    elif short(x) == True:
        print("$20")
    else:
        print("$100")

def short(n):
    z = n.find("h")
    if z == 0:
        return True

main()


