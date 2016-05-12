def main():

    answer = 0
    triangles = set([])
    # generate triangle numbers
    n = 1
    i = 1
    while i < 800:
        triangles.add(i)
        n += 1
        i = int((n/2)*(n + 1))

    myfile = open('./Problems 40-49/words.txt')

    for word in myfile.read().split(','):

        word = word.strip('"')
        number = wordnum(word)

        if number in triangles:
            answer += 1

    myfile.close()

    print(answer)

def wordnum(word):
    total = 0

    for i in word:
        total += ord(i) - 64

    return total

main()
