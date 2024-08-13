def main():
    d = dict()
    list = []
    s_list = []
    try: #build list from user input
        while True:
            x = input().upper()
            list.append(x)
            s_list = sorted(list)

    except EOFError: #return output
         for x in s_list:
                if x not in d:
                    d[x] = 1

                else:
                    value = d[x]
                    value = value + 1
                    d[x] = value
         print()
         for x in d:
              print(d[x], x)

main()



