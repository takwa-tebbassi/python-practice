def fibonacci(n) :

    suite = []
    x0 = 0
    x1 = 1

    suite.append(x0)
    suite.append(x1)

    for i in range(2,n):
        
        x2 = x1 + x0
        x0 = x1
        x1 = x2
        suite.append(x2)
        
    return(suite)
    
# main program

n = int(input("enter an integer: "))

print("the first",n,"terms of fibonacci : ", fibonacci(n))