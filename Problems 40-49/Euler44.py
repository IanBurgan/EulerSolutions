from math import sqrt

def main():
    # 5000 is an arbitrary limit
    for i in range(1, 5000):
        for j in range(i + 1, 5000):
            numi = i * (3 * i - 1) // 2
            numj = j * (3 * j - 1) // 2
            if test(numj - numi) and test(numj + numi):
                print(numj - numi)
                # returning to break both loops
                return

# tests a number to see if it is pentagonal
def test(num):
    # finds the base, rounds to a natural number
    base = int((sqrt(24 * num + 1) + 1) / 6)
    # calculates the pentagonal number of the base
    num2 = base * ((3 * base) - 1) // 2
    # compares to see if the base was rounded
    return num == num2

main()
