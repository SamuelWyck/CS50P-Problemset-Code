def main():
    math = input("Expression: ")
    x, y, z = math.split(" ")
    x2 = int(x)
    z2 = int(z)
    if y == "+":
        t = x2 + z2
    elif y == "-":
        t = x2 - z2
    elif y == "*":
        t = x2 * z2
    elif y == "/":
        t = x2 / z2
    h = float(t)
    print(f"{h:.1f}")
main()
