from math import *

def PGCD (a,b):

    div = []
    divA = []
    divB = []

    for i in range(1,a):
        if a % i == 0:
            divA.append(i)
    
    for j in range(1,b):
        if b % j == 0:
            divB.append(j)


    for d in divA:
        for d2 in divB:
            if d == d2:
                div.append(d)

    return(max(div))



# main prog

a = int(input("enter an integer : "))
b = int(input("enter an integer : "))

print("le pgcd de",a,"et",b,"=",PGCD(a,b))