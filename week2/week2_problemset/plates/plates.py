def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if req1(s) == True and req2(s) == True and req3(s) == True and req4(s) == True:
        return True
    else:
        return False

def req1(n):
    c = n[0:2]
    if c.isalpha() == True:
        return True
    else:
        return False
#
def req2(n):
    if len(n) >= 2 and len(n) <= 6:
        return True
    else:
        return False
#no punctuation
def req3(n):
    if n.isalnum() == True:
        return True
    else:
        return False

def req4(n):
    for c in n:
        if c.isdigit() == True:
               g = int(n.index(c))
               x = n[g:None]
               if x.isdigit() == True and x[0:1] != "0":
                   return True
               else:
                   return False
    return True

main()
