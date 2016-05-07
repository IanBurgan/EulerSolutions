# Not the best solution but works to solve the problem.
# One of my least favorite so far.

def main():
    names = {0 : "", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", \
    6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten", 11 : "eleven", \
    12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", \
    17 : "seventeen", 18 : "eighteen", 19 : "nineteen", 20 : "twenty", 30 : "thirty", \
    40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}

    # count the length of each number string
    total = 0
    for i in range(1001):
        total += count(i, names)
    print(total)

def count(number, names):
    total = 0
    # for single digit numbers just look up the digit
    if len(str(number)) == 1:
        total += len(names[number])
    # for 2 digit numbers handle teens and 20 upwards
    elif len(str(number)) == 2:
        if number < 20:
            total += len(names[number])
        else:
            tens = int(str(number)[0] + "0")
            ones = int(str(number)[1])
            total += len(names[tens]) + len(names[ones])
    # for 3 digit numbers handle "hundred and" for each case
    elif len(str(number)) == 3:
        hun = int(str(number)[0])
        total += len(names[hun])
        total += len("hundred")
        tens = str(number)[1:]
        if tens != "00":
            total += len("and")
            if int(tens) < 20:
                total += len(names[int(tens)])
            else:
                total += len(names[int(tens[0] + '0')])
                total += len(names[int(tens[1])])
    elif len(str(number)) == 4:
        total += len("onethousand")
    return total

main()
