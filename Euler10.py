def main():
    limit = 2000000
    total = 0

    primes = [True] * limit
    primes[0], primes[1] = False, False

    # eliminate all the even numbers
    for i in range(4, len(primes), 2):
        primes[i] = False

    # sieve eliminating all multiples of lower primes
    for (i, isPrime) in enumerate(primes):
        if isPrime:
            total += i
            for j in range(i*i, limit, 2*i):
                primes[j] = False

    print(total)

main()
