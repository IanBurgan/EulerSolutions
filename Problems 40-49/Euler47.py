def main():
    # ugly brute force solution. better solution involves generating the numbers
    # from prime factos
    i = 210
    found = False

    while not found:
        if factors(i) == 4:
            if 4 == factors(i - 3) == factors(i - 2) == factors(i - 1):
                print(i - 3)
            if 4 == factors(i + 1) == factors(i + 2) == factors(i + 3):
                print(i)
        i += 4

def sieve(limit):
    primes = [True] * limit
    if limit > 1:
        primes[0], primes[1] = False, False

    # eliminate all multiples of 2
    for i in range(4, len(primes), 2):
        primes[i] = False
    # eliminate all multiples of primes
    for (i, isPrime) in enumerate(primes):
        if isPrime:
            for j in range(i * i, limit, 2 * i):
                primes[j] = False
    return {x for x in range(len(primes)) if primes[x]}

# counts number of prime factors using sieve
def factors(number):
    total = 0

    for i in sieve((number // 2) + 1):
        if number % i == 0:
            total += 1

    return total

main()
