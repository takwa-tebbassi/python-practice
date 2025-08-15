def supprDoubl(lis):
    
    length = len(lis)
    i = 0
    j = 1
    while i < len(lis)-1:
            while j < len(lis):
                if lis[i] == lis[j]:
                    del lis[j]
                    i+=1
                    j+=1

                else:
                    i+=1
                    j+=1

    return lis


# main prog

lis = []
for i in range(5):
    x = int(input("enter int: "))
    lis.append(x)


print(supprDoubl(lis))