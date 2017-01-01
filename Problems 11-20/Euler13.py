def main():
    # open the file and read the data
    infile = open("./Problems 10-19/problem13.txt")
    nums = infile.read().split('\n')
    del nums[-1]

    # sum the first 13 digits just to be safe
    total = 0
    for i in nums:
        total += int(i[:13])
    
    print(str(total)[:10])
    infile.close()

main()
