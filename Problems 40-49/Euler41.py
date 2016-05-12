from math import sqrt
from itertools import permutations

def main():
    digits = ['1', '2', '3', '4', '5', '6', '7']

    pans = list(permutations(digits, 7))
    pans.reverse()

    for num in pans:
        # each permutation is a tuple
        temp = int(''.join(num))
        if isPrime(int(temp)):
            print(temp)
            break

def isPrime(number):
    if number % 2 == 0 or number == 1:
        return False
    for i in range(3, int(sqrt(number) + 1), 2):
        if number % i == 0:
            return False
    return True

main()
