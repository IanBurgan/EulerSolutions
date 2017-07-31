def main():
    total = 0

    for i in range(1, 10000):
        if not test(i, 1):
            total += 1

    print(total)

def test(num, it):
    if it > 49:
        return False
    else:
        check = num + int(str(num)[::-1])
        if isDrome(check):
            return True
        else:
            return test(check, it + 1)

def isDrome(num):
    return str(num) == str(num)[::-1]

main()
