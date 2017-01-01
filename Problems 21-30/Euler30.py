def main():
    total = 0
    # limit of 1000000 becuase 999999 > (9 ** 5) * 5
    for i in range(2,1000000):
        sumofdigits = 0
        number = str(i)
        for j in number:
            sumofdigits += int(j)**5
        if sumofdigits == i:
            total += i

    print(total)

main()
