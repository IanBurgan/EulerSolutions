def main():
    total = 0

    for n in range(1001, 0, -1):
        # diagonals are always odd
        if n % 2 != 0 and n > 1:
            # each upper right is the row length squared
            # the other four corners are jsut offset based upon row length
            total += n**2
            total += n**2 - (n-1)
            total += n**2 - 2*(n-1)
            total += n**2 - 3*(n-1)
    total += 1

    print(total)

main()
