def main():
    a = 50
    print(f"Amount Due: {a}")
    while a > 0:
        x = int(input("Insert Coin: "))
        if coin_check(x) == False:
            x = 0
        else:
            x = coin_check(x)
        a = a - x
        if a > 0:
            print(f"Amount Due: {a}")
        elif a <= 0:
            a = a * -1
            print(f"Change Owed: {a}")
            break

def coin_check(c):
    match c:
        case 25 | 10 | 5:
            return c
        case _:
            return False
main()
