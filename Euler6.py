def main():
    # totals for the two numbers
    squares = 0
    total = 0
    # loop through 1-100
    for i in range(1, 101):
        squares += i**2
        total += i
    print(total**2 - squares)

main()
