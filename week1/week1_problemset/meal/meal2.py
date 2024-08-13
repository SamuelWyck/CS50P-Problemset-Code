def main():
    x = input("What time is it? ")
    y = convert(x)
    if y >= 7 and y <= 8:
        print("breakfast time")
    elif y >= 12 and y <= 13:
        print("lunch time")
    elif y >= 18 and y <= 19:
        print("dinner time")

def convert(n):
    x, y = n.split(":")
    hr = float(x)
    min = float(y)
    mins = min / 60
    time = hr + mins
    return time

if __name__ == "__main__":
    main()

