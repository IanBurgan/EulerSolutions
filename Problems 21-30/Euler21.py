from math import sqrt

def main():
    total = 0

    for i in range(1, 10000):
        other = sumfactors(i)
        if i == sumfactors(other):
            if i != other:
                total += i + other

    print(total/2)


def sumfactors(x):
    total = 1
    for i in range(2, int(sqrt(x) + 1)):
        # add all factors found to the total
        if x % i == 0:
            total += i
            if i != x // i:
                total += x // i
    return total

main()
