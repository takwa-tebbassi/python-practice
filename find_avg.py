from math import*
import numpy

def average():
    T = []
    test = True
    q = 'n'

    while test and q == 'n':
        x = int(input("\nenter an integer: "))
        T.append(x)
        
        q = input("are you done yet (y/n) ?")
        if (q == 'y'):
            test = False
        elif (q == 'n'):
            test = True
        else:
            q = input("the answer should be 'y' or 'n': ")
    
    
    avg = numpy.average(T)
    return (avg)




# main program
avg = average()
print("The list average is:", avg)
