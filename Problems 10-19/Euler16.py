def main():
    # the number
    a = 2 ** 1000
    a = str(a)
    # loop over its digits adding them to total
    total = 0
    for i in a:
        total += int(i)
    print(total)

main()
