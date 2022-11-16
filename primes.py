"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 2
    isPrime = True
    doneSearch = False
    if (number_of_primes <= 0):
        raise ValueError("invalid number")
    else:
        while (len(list) < number_of_primes):
            while(isPrime == True and doneSearch == False):
                for i in range(2, number):
                    if (i is not number):
                        if (number%i == 0):
                            isPrime = False
                doneSearch = True
            if(isPrime == True):
                list.append(number)

            number= number + 1
            isPrime = True
            doneSearch = False

    return list
