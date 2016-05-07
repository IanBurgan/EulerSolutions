def main():
    # a must be under 333 because a < b < c and a + b + c = 1000
    for a in range(1, 333):
        for b in range(a, 500):
            c = 1000 - (a + b)
            # check to see if it's a triple
            if (a * a) + (b * b) == (c * c):
                print(a * b * c)

main()
