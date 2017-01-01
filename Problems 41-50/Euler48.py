def main():
    # continually add to the total. Print out the last 10 digits
    total = 0
    for i in range(1,1001):
        total += i ** i

    print(str(total)[-10:])

main()
