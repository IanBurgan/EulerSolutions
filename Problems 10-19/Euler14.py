def main():
    # length of max chain
    largest = 0
    # start of max chain
    start = 10

    i = 10
    # max start is 1 million
    while i < 1000000:
        length = 1
        num = i
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num * 3 + 1
            length += 1
        if length > largest:
            largest = length
            start = i
        i += 1

    print(start)

main()
