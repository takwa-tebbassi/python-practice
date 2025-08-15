def findingSec(lis):

    maxi  = 0
    max2 = 0

    for number in lis:
        if number > maxi:
            maxi = number
    
    for number in lis:  
        if number > max2 and number < maxi:
            max2 = number


    return(max2)


# main prog

lis = []

for i in range(5):
    x = int(input("enter an int: "))
    lis.append(x)

print(lis)


print("the second big in ur list:",findingSec(lis))



        

