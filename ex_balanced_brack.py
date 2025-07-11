#Check if a string of brackets is balanced

def is_balanced(s):
    
    a = False
    b = False
    c = False

    if (s.count('{') == s.count('}')):
        a = True
    if (s.count('(') == s.count(')')):
        b = True
    if (s.count('[') == s.count(']')):
        c = True

    if (a and b and c):  # is balanced
        return(True)
    else:
        return(False)

# main program

s = input("enter brackets")
x = is_balanced(s)
print(x)