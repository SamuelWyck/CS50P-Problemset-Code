def main():
    x = input("File name: ").lower()

    if gif(x) == True:
        print("image/gif")
    elif jpg(x) == True:
        print("image/jpeg")
    elif png(x) == True:
        print("image/png")
    elif pdf(x) == True:
        print("application/pdf")
    elif txt(x) == True:
        print("text/plain")
    elif zip(x) == True:
        print("application/zip")
    else:
        print("application/octet-stream")

def gif(n):
    y = n.find(".gif")
    if y != -1:
        return True

def jpg(n):
    y = n.find(".jpg")
    z = n.find(".jpeg")
    if y != -1 or z != -1:
        return True

def png(n):
    y = n.find(".png")
    if y != -1:
        return True

def pdf(n):
    y = n.find(".pdf")
    if y != -1:
        return True

def txt(n):
    y = n.find(".txt")
    if y != -1:
        return True

def zip(n):
    y = n.find(".zip")
    if y != -1:
        return True

main()
