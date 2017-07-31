def main():

    large = 0

    for a in range(1, 100):
        for b in range(1, 100):
            exp = a**b
            digits = digSum(exp)
            if digits > large:
                large = digits

    print(large)
def digSum(num):
    return sum([int(x) for x in str(num)])


main()
