def main():
    total = 0

    #first two terms in the sequence
    i = 1
    j = 2
    # the terms under four million
    while j < 4000000:
        #add even terms to the total
        if i % 2 == 0:
            total += i
        if j % 2 == 0:
            total += j

        #increment the terms
        i = i + j
        j = i + j

    print(total)

main()
