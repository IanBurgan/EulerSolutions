from string import ascii_uppercase

def main():
    total = 0

    infile = open("./Problems 20-29/problem22.txt")
    names = infile.read().split(",")
    names.sort()

    for i in range(len(names)):
        total += (i + 1) * score(names[i])

    print(total)

def score(name):
    total = 0
    for i in name:
        total += ascii_uppercase.index(i) + 1
    return total

main()
