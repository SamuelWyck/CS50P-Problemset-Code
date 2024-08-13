from PIL import ImageOps
from PIL import Image
import sys
import os.path

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif sys.argv[1].lower().find(".png") == -1 and sys.argv[1].lower().find(".jpeg") == -1 and sys.argv[1].lower().find(".jpg") == -1:
        print("Invalid input")
        sys.exit(1)
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        print("Input and output have different extensions")
        sys.exit(1)

    try:
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])
        image = ImageOps.fit(image, [600, 600])
        image.paste(shirt, shirt)
        image.save(sys.argv[2])
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()

