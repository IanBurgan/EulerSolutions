def main():
    # open the file and read the data (newlines removed)
    infile = open("./Problems 1-9/problem8.txt")
    number = infile.read().replace('\n', '')

    # for the max found
    biggest = 0

    # looping over the number and calculating the product of the 13 digits
    for i in range(len(number) - 12):
        prod = product(number[i:i+13])

        if prod > biggest:
            biggest = prod

    print(biggest)
    infile.close()

# calculates the product of all digits in a string
def product(mystring):
    total = 1
    for i in mystring:
        total *= int(i)
    return total

main()
