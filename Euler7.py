def main():
    # x/ln(x) determines the number of primes under a given number
    # 12586 primes are under 150000 (1.5 * 10^5) according to equation
    limit = 150000

    primes = [True] * limit
    primes[0], primes[1] = False, False

    trueprimes = []
    # sieve eliminating all multiples of lower primes
    for (i, isPrime) in enumerate(primes):
        if isPrime:
            trueprimes.append(i)
            for j in range(i*i, limit, i):
                primes[j] = False

    # 0 is the first prime 10000 is the the 10001st prime
    print(trueprimes[10000])

main()
