def main():
    positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1
    empty = ""

    for i in range(1000000):
        empty += str(i)

    for i in positions:
        product *= int(empty[i])

    print(product)

main()
