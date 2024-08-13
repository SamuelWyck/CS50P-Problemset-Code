def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    date = input("Date: ")
    while True:
        try: #handle date in month d, yyy
            x, y, z = date.split(" ")
            if x.isdigit() == True:
                date = input("Date: ")
            w = int(months.index(x))
            q = w + 1
            if y.find(",") == -1:
                date = input("Date: ")
            y = int(y.removesuffix(","))
            if y > 31:
                date = input("Date: ")
            else:
                print(f"{z}", f"{q:02}", f"{y:02}", sep="-")
                break
        except ValueError: #handle m/d/y
            x, y, z = date.split("/")
            if x.isdigit() == False or y.isdigit() == False or z.isdigit() == False:
                date = input("Date: ")
            y = int(y)
            x = int(x)
            if y > 31 or x > 12:
                date = input("Date: ")
            else:
                print(f"{z}", f"{x:02}", f"{y:02}", sep="-")
                break
main()
