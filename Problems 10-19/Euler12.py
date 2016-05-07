def main():
    i = 2
    num = 1

    while factors(num) < 500:
        num += i
        i += 1

    print(num)

# Will not return the correct number for perfect squares as it does not
# check the square root of the number.
def factors(num):
    facs = 0
    for i in range(1, int(num ** 0.5)):
        if num % i == 0:
            facs += 2

    return facs

main()
