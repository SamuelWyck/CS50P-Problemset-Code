# for loops
#for _ in range(3):
 #   print("meow")

# while loops
#i = 0
#while  i < 3:
 #   print("meow")
  #  i += 1

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
main()
