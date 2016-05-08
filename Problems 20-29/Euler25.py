def main():

    too_low_digits = True

    new = 1
    old = 1
    counter = 2
    # continually generating terms until one of length is found
    while too_low_digits:
        new += old
        old = new - old
        counter += 1
        if len(str(new)) >= 1000:
            too_low_digits = False

    print(counter)

main()
