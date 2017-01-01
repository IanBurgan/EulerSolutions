def main():
    # 546 is max length. sum(first 547 primes) > 1000000. not true for 546
    num = 546
    extra = 0
    primes = nPrimes(num)

    while not isPrime(sum(primes)):
        if sum(primes) > 1000000:
            extra = 0
            num -= 1
        extra += 1
        primes = nPrimes(num + extra)

        # removing bottom of sequence until it is correct length
        for i in range(extra):
            primes.discard(min(primes))

    print(sum(primes))

# terrible way to generate n primes, but it works for this
def nPrimes(n):
    limit = 6 * n
    primes = sieve(limit)

    while len(primes) > n:
        limit -= 2
        primes = sieve(limit)
    while len(primes) < n:
        limit += 2
        primes = sieve(limit)

    return primes

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
    return {x for x in range(len(primes)) if primes[x]}

def isPrime(n):
    # base cases
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    # primes all take form of 6k + 1 or 6k - 1
    # test by all numbers of this form (aka possible primes) below sqrt of n
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


main()
