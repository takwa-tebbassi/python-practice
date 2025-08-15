from math import*

def tri_length(sentence):
    
    
    # to sort a list of words by the first letter order in alphabet
    # sorted("This is a test string from Andrew".split(), key=str.casefold)

    # lis = sorted(lis.split())   # a simple split by blank with sort
    
    words = sentence.split()
    lis = sorted(words, key=len)

    return lis



# main prog

sentence = input("enter a sentence: ")
print(tri_length(sentence))
