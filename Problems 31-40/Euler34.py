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
    total = 0
    num2 = num
    while num2 > 0:
        total += facts[num2 % 10]
        num2 = num2 // 10

    if num == total:
        return True

    return False

main()
