def sumDigits(num):

    x = 0
    s = str(num)
    for number in s:
        number = int(number)
        x += number
    return(x)


# main prog

num = int(input("enter an integer : "))
print("the sum of",num,"is",sumDigits(num))