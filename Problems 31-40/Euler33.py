def main():
    numerator = 1
    denominator = 1
    # All answers take the form ax/xb = a/b
    # ax / bx is a trivial example
    # xa / xb will never equal a / b without a == b
    # xa / bx is the inverse of (bx / xa) which is a rename of (ax / xb) and
    # will not be less than 1
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for x in range(a + 1, 10):
                ax = (a * 10) + x
                xb = (x * 10) + b
                if (ax / xb) == (a / b):
                    numerator *= a
                    denominator *= b
    # assuming the fraction reduces to 1 / something
    print(denominator // numerator)

main()
