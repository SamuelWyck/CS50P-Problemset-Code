from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

def main():
    #make sure input is correct length

    if len(sys.argv) == 1:
            r = input("Input: ")
            figlet.setFont(font=(random.choice(figlet.getFonts())))
            print(figlet.renderText(r))

    elif len(sys.argv) > 3 or sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid useage")
        sys.exit(1)

    elif len(sys.argv) == 3:
        y = sys.argv[2]
        if y not in figlet.getFonts():
            print("Invalid useage")
            sys.exit(1)

        x = input("Input: ")
        figlet.setFont(font=y)
        print(figlet.renderText(x))

    else:
         print("Invalid useage")
         sys.exit(1)

if __name__ == "__main__":
    main()


