#Given a sentence, return the longest word

def find_longest_word(sentence):
    maxi = 0
    newS = sentence.split(" ")
    for word in newS:
        length = len(word)
        if len(word) > maxi:
            newWord = word
            maxi = length
    print(newWord,' | ', maxi)


# main program

sentence = input("give a sentence: ")
find_longest_word(sentence)