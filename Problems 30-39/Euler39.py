def main():
    pvals = dict((i, 0) for i in range(1, 1001))
    # c and b must be greater than a
    for a in range(1, 333):
        for b in range(a, 500):
            c = int((a ** 2 + b ** 2) ** (1/2))
            if a + b + c <= 1000 and a ** 2 + b ** 2 == c ** 2:
                pvals[a + b + c] += 1
    # use the lists of keys and values to
    # find the key associated with the max value
    answers = list(pvals.keys())
    amounts = list(pvals.values())

    print(answers[amounts.index(max(amounts))])
main()
