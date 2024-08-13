def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            z = ((x / y) * 100)
            if z >= 99 and z <= 100:
                print("F")
                break
            elif z > 100:
                None
            elif z <= 1:
                print("E")
                break
            else:
                print(f"{z}%")
                break
        except (ValueError, ZeroDivisionError):
            pass

main()
