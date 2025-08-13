def occ_liste(L):

    thisdict = {}
    L  = L.split(",")
    for number in L:
        occ = L.count(number)
        thisdict[number] = occ

    print(thisdict)

# main prog

L = input("enter a list of numbers (seprated by ','): ")
occ_liste(L)