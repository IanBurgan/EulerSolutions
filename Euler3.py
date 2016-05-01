def main():
    # the number to be factored
    number = 600851475143
    # starting with 3 because the number is not even
    div = 3

    while div < number:
        if number % div == 0:
            # reduce the number everytime a prime factor is found
            number = number // div
        else:
            # otherwise increase the divisor
            div += 2

    print(number)
main()
