def main():
    total = 0

    #loop over the numbers under 1000
    for i in range(1000):
        if i % 5 == 0 or i % 3 == 0:
            total += i

    print(total)

main()
