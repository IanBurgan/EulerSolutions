from math import factorial
# 9,999,999 > 7 * 9!
# 7 * 9! = 2540160 so no numbers less than this need to be checked

def main():
    # a list to look up factorial values instead of repeatedly calculate
    factorials = []
    total = 0
    # populate the factorial list
    for i in range(0, 10):
        factorials.append(factorial(i))

    for i in range(3, 2550000):
        if check(i, factorials):
            total += i

    print(total)

def check(num, facts):
    string = str(num)
    total = 0

    for i in string:
        total += facts[int(i)]

    if num == total:
        return True

    return False

main()
