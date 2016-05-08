from math import sqrt

def main():
    ans = set()
    total = 0
    for i in range(1, 28123):
        # if the number is abundant
        if sumfactors(i) > i:
            ans.add(i)
        # if no two abundants sum to the number
        if not any((i - j) in ans for j in ans):
            total += i

        # The commented out code produces the same result that "any" does
        # but is much slower. It has been included so that the code above can
        # be better understood.

        # found = False
        # for j in ans:
        #     num = i - j
        #     if num in ans:
        #         found = True
        # if not found:
        #     total += i

    print(total)

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
