def main():
    # the first digit will be a 9
    for i in range(9876, 9123, -1):
        # where the products will be added
        temp = ""
        count = 1

        while len(temp) < 9:
            temp += str(i * count)
            count += 1

        if isPandigital(temp):
            break

    print(temp)

def isPandigital(mystring):
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if len(mystring) != 9 or not all(x in mystring for x in digits):
        return False
    return True

main()
