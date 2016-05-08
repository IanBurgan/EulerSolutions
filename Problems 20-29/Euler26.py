def main():
    answer = 7
    largest = 6
    # loop and continually update answer when a longer cycle is found
    for d in range(1,1000):
        length = period(d)
        if length > largest:
            largest = length
            answer = d
    print(answer)

def period(d):
    # divide by 5 and 2 because they are the prime factors of 10 (base 10)
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    for num in range(1, d):
        # repeating decimals have denominators like 9, 99, 999, ...
        # the number of 9's in the denominator is the cycle length
        if ((10 ** num) - 1) % d == 0:
            return num
    return 0

main()
