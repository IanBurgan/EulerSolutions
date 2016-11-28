from math import sqrt

def main():
    possible_b = sieve(1000)
    answer = 0
    longest = 0
    for a in range(-1000, 1000):
        # because 0 is the starting point b must be prime
        for b in possible_b:
            n = 0
            result = n ** 2 + a * n + b
            while result > 0 and isPrime(result):
                n += 1
                result = n ** 2 + a * n + b

            if n > longest:
                longest = n
                answer = a * b

    print(answer)

def sieve(limit):
    primes = [True] * limit
    primes[0], primes[1] = False, False

    # eliminate all multiples of 2
    for i in range(4, len(primes), 2):
        primes[i] = False
    # eliminate all multiples of primes
    for (i, isPrime) in enumerate(primes):
        if isPrime:
            for j in range(i * i, limit, 2 * i):
                primes[j] = False

    return [x for x in range(len(primes)) if primes[x]]
# checks a number for primality by testing divisors
def isPrime(number):
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number) + 1), 2):
        if number % i == 0:
            return False
    return True

main()
