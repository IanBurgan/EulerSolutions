from math import sqrt

def main():
    # generate triangle numbers and test each
    n = 40755
    num = n * (n + 1) // 2
    while not test(num):
        n += 1
        num = n * (n + 1) // 2
    print(num)

# tests a number to see if it is pentagonal and hexagonal
def test(num):
    # find the base if it is pentagonal, rounds to a natural number
    base = int((sqrt(24 * num + 1) + 1) / 6)
    # calculates the pentagonal number of the base
    num2 = base * ((3 * base) - 1) // 2
    # compares to see if the base was rounded
    flag1 = num == num2
    # find the base if it is hexagonal, rounds to a natural number
    base = int((sqrt(8 * num + 1) + 1) / 4)
    # calculates the hexagonal number of the base
    num2 = base * (2 * base - 1)
    # compares to see if the base was rounded
    flag2 = num == num2

    return flag1 and flag2

main()
