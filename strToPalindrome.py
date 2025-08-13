def strPal(c):

    res = c
    if len(c) % 2 == 0:
        for i in range(len(c)-1,-1,-1):
            res = res + c[i]

    else:
        for i in range(len(c)-2,-1,-1):
            res = res + c[i]

    return res



# main prog

c = input("enter a word: ")
print(c,"becomes: ",strPal(c))