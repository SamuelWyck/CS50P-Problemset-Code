import emoji

def main():
    x = input("Input: ")
    print("Output:", emoji.emojize(x, language="alias"))

if __name__ == "__main__":
    main()
