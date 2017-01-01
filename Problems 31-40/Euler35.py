def main():
    counter = 0
    primes = sieve(1000000)
    for i in primes:
        others = rotations(i)
        # all rotations must be prime
        if all(x in primes for x in others):
            counter += 1

    print(counter)

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

def rotations(number):
    original = str(number)
    others = set()
    if len(original) == 1:
        return set([number])
    for i in range(1, len(original)):
        new = original[i:] + original[:i]
        others.add(int(new))
    return others

main()
