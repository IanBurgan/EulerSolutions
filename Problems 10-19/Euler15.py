from math import factorial
def main():
    # This is the formula for 40 choose 20.
    # 40 choose 20 is used because each path involves going right 20
    # and down 20 in one order or another. With these 40 steps, we must
    # choose which 20 of them are right steps (or down steps). Essentially
    # all 40 slots for moves have been put into a bag. We then pulled 20
    # of them out at random. These slots were then filled with moves to
    # the right. The other remaining slots are then filled with moves
    # down. How many different ways there are to choose these 20 moves
    # is equivalent to how many paths there are.
    print(factorial(40)/(factorial(20) ** 2))
main()
