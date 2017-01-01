def main():
    i, j = 999, 999
    biggest = 0

    # 500 because we are assuming it is in the top half
    while i > 500:
        # later found palindromes may be greater
        if isPalindrome(i*j) and (i*j) > biggest:
            biggest = i*j

        j -= 1
        if j < 100:
            i -= 1
            j = i

    print(biggest)

def isPalindrome(num):
    num2 = str(num)
    return num2[::-1] == num2

main()
