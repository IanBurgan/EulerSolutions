from math import sqrt

def main():
    start = [2, 3, 5, 7]
    odds = [1, 3, 5, 7, 9]
    rights = []
    truncs = []

    # find 2 digit truncatables
    for i in start:
        for j in odds:
            num = (i * 10) + j
            if isPrime(num):
                rights.append(num)

    # find all right truncatables
    for i in rights:
        for j in odds:
            num = (i * 10) + j
            if isPrime(num):
                rights.append(num)
    # check all right truncatables for left truncatables
    for i in rights:
        if isLeft(i):
            truncs.append(i)

    print(sum(truncs))

def isLeft(number):
    amount = 10
    while number % amount != number:
        if not isPrime(number % amount):
            return False
        amount *= 10
    return True

def isPrime(number):
    if number % 2 == 0 or number == 1:
        return False
    for i in range(3, int(sqrt(number) + 1), 2):
        if number % i == 0:
            return False
    return True

main()
