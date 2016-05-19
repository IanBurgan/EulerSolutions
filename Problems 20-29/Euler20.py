def main():
    number = factorial(100)
    total = 0
    for i in str(number):
        total += int(i)

    print(total)

def factorial(num):
    total = 1
    while num > 1:
        total *= num
        num -= 1
    return total

main()
