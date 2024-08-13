def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    short = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return short


if __name__ == "__main__":
    main()
