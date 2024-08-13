def main():
    while True:
        fraction = input("Fraction: ")
        convert(fraction)
        if convert(fraction) == "no":
            None
        else:
            break
    print(gauge(convert(fraction)))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        percentage = round(((x / y) * 100))
        if x > y:
                raise ValueError
        return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(z):
    if z >= 99 and z <= 100:
        return "F"
    elif z <= 1:
        return "E"
    else:
        return f"{z}%"

if __name__ == "__main__":
    main()
