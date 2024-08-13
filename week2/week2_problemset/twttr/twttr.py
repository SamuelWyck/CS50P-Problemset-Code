def main():
    x = input("Input: ")
    remove_vowels(x)

def remove_vowels(v):
    print("Output: ", end="")
    for c in v:
        match c:
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                None
            case _:
                print(c, end="")
    print()

main()

