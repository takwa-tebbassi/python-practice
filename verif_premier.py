def verifPremier(x) :

    test = True

    for i in range(2, x//2):
        if x % i == 0 :
            test = False

    if test == True:
        print(x," est premier")

    else:
        print(x," n'est pas premier")
        




# main program

x = int(input("donner un entier : "))

verifPremier(x)