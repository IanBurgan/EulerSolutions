import math

def main():
    total = 0
    n0, n1 = 3, 7
    d0, d1 = 2, 5

    for i in range(2,1000):
        num = n1 * 2 + n0
        den = d1 * 2 + d0
        n0 = n1
        d0 = d1
        n1 = num
        d1 = den

        if math.floor(math.log10(num)) + 1 > math.floor(math.log10(den)) + 1:
            total += 1

    print(total)
main()
