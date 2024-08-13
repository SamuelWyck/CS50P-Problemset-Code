def main():
    x = float(input("What's x? "))
    print("x squared is", round(square(x)))

def square(n):
    return(pow(n, 2))
main()
