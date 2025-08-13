from math import*

def equation(a,b,c):

    delta = b**2  - 4 * a * c

    if delta > 0:
        print("deux racines réelles: ")
        x1 = (-b - sqrt(delta)) / 2*a
        x2 = (-b + sqrt(delta)) / 2*a
        print(x1," | ",x2)

    elif delta == 0:
        print("y a une racine: ")
        x1 = -b / 2*a
        print(x1)

    else:
        print('pas de racine réelle: ')
        print('{}')


# main prog

print("\n    ---------  L'équation ax² + bx + c  ------- ")

a = int(input("donner a: "))
b = int(input("donner b: "))
c = int(input("donner c: "))

print("Les racines de l'équation",a,"x² +",b,"x +",c," : ")
equation(a,b,c)
print("\n")