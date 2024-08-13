import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r".+https?://(?:www\.)?youtube\.com/embed/(\w+).*", s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"

if __name__ == "__main__":
    main()
