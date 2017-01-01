def main():
    total = 0

    for i in range(1, 1000000):
        string = str(i)
        # the binary version of the number (cut off the 0b)
        string2 = bin(i)[2:]
        # it's palindromic if it's the same in reverse
        if string == string[::-1] and string2 == string2[::-1]:
            total += i
    print(total)

main()
