from math import factorial

def main():
    permutation = 1000000

    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    answer = ""

    # current is how deep we are into the permutations
    current = 0
    # the position in the digits list
    position = 0

    # The first 9! permutations start with 0, the next 9! with 1 and so on.
    # After determing the first digit the same concept is used on all digits
    while len(digits) > 0:
        # if the permutation we are looking for is deeper than the digit we are on
        if factorial(len(digits) - 1) + current < permutation:
            current += factorial(len(digits)-1)
            position += 1
        # if we are within the bounds of the permutations for the current digit
        elif factorial(len(digits)-1) + current >= permutation:
            answer += digits.pop(position)
            position = 0

    print(answer)
main()
