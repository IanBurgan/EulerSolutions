def main():
    pandigitals = set()

    # one digit numbers must go with 4 digit numbers
    for i in range(10):
        for j in range(1000, 10000):
            combo = str(i) + str(j) + str(i*j)
            if isPan(combo):
                pandigitals.add(i * j)
    # two digit numbers must go with 3 digit numbers
    for i in range(10, 100):
        for j in range(100, 1000):
            combo = str(i) + str(j) + str(i*j)
            if isPan(combo):
                pandigitals.add(i * j)

    print(sum(pandigitals))
# checks that all digits are in the number
def isPan(string):
    if len(string) != 9:
        return False
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if any(i not in string for i in nums):
        return False
    return True

main()
