def main():
    x = input("What time is it? ")
    z = x.find("a.m.")
    q = x.find("p.m.")
    if z != -1:
        n, t = x.split(" ")
        i = convert(n)
        if i >= 7 and i <= 8:
            print("breakfast time")
    if q != -1:
        w, e = x.split(" ")
        u = convert(w)
        if u >= 12 and u < 13 or u == 1:
            print("lunch time")
        elif u >= 6 and u <= 7:
            print("dinner time")
    else:
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
