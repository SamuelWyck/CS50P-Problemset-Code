def convert(x):
    y = x.replace(":)","🙂").replace(":(","🙁")
    return y

def main():
    x = input("Type here: ")
    y =  convert(x)
    print(y)

main()
