from itertools import permutations

def main():
    primes = sieve(10000)
    # copy to check if a number is prime
    possibles = primes.copy()

    while len(possibles) > 0:
        # continually remove a prime from the set
        prime = possibles.pop()
        # a set of permutations of the prime
        perms = {''.join(perm) for perm in permutations(prime)}

        # for all permutations of the prime
        for num in perms:
            # if the permutation is less and also prime
            if num < prime and num in primes:
                # use the difference to find the third term in sequence
                diff = int(prime) - int(num)
                third = str(int(num) - diff)
                # if the third term is a permutation and prime
                if third in perms and third in primes:
                    # print the answer
                    print(third + num + prime)

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
    # MODIFIED TO EXCLUDE 3 DIGIT NUMBERS AND RETURN STRINGS
    return {str(x) for x in range(len(primes)) if primes[x] and x > 1000}

main()
