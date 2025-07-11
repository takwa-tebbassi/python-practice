def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


def fizzbuzz_twist():
    
    prime = 0

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")
        
        if is_prime(i):
            print(i, "Prime")
                

# main program

fizzbuzz_twist()