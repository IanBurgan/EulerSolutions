from math import sqrt

def main():
    # arbitrary guess of 10000
    for i in range(33, 10000, 2):
        found = False
        # looping over squares
        for j in range(1, int(i ** 0.5)):
            num = (j ** 2) * 2
            # check the difference for primality
            if num < i and isPrime(i - num):
                found = True
        # if no combination found break and print
        if not found and not isPrime(i):
            print(i)
            break

def isPrime(number):
    if number % 2 == 0 or number == 1:
        return False
    for i in range(3, int(sqrt(number) + 1), 2):
        if number % i == 0:
            return False
    return True

main()
