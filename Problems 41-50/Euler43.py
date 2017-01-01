def main():
    # this is lengthy and more analysis than code
    primes = [2, 3, 5, 7, 11, 13, 17]
    # d2d3d4 - 2, d3d4d5 - 3, d4d5d6 - 5, d5d6d7 - 7
    # d6d7d8 - 11, d7d8d9 - 13, d8d9d10 - 17
    # d6 must always be a 5 or a 0.
    # if d6 was a 0, d6d7d8 could not be pandigital and divisible by 11
    # 011, 022, 033 and so on...
    # We now know that d6 will always be 5
    # using this lets narrow down d6d7d8
    possibles = []
    for i in range(500, 600):
        num = str(i)
        if num[0] != num[1] and num[1] != num[2] and num[0] != num[2]:
            if i % 11 == 0:
                possibles.append(i)
    # using this limited list for d6d7d8 [506, 517, 528, 539, 561, 572, 583, 594]
    # we can now determine d9 using the multiples of 13
    del possibles[0]    # we can remove 506 because 13 * 5 = 065
    del possibles[0]    # we can remove 517 because 13 * 13 = 169
    possibles[0] = 5286    # 528 is the first 3 digits of 5286. 13 * 22 = 286
    possibles[1] = 5390    # 539 is the first 3 digits of 5390. 13 * 30 = 390
    del possibles[2]    # we can remove 561 because 13 * 47 = 611
    possibles[2] = 5728 # 13 * 56 = 728
    possibles[3] = 5832 # 13 * 64 = 832
    del possibles[-1] # 13 * 73 = 949
    # we can repeat the same process for 17 that we did for 13
    possibles[0] = 52867 # 17 * 51 = 867
    possibles[1] = 53901 # 17 * 53 = 901
    possibles[2] = 57289 # 17 * 17 = 289
    del possibles[3] # 17 * 19 = 323
    # using a similar process we can find multiples of 7 that end appropriately
    # 952 is the only multiple of 7 that ends in 52 without repeating a digit
    # there are no valid multiples of 7 that end in 53
    # 357 is the only valid multiple of 7 that ends in 57
    possibles[0] = 952867
    del possibles[1]
    possibles[1] = 357289
    # we will skip 5 and 3 for now because they don't help narrow things down
    # the next digit must be even becuase d2d3d4 is divisible by 2
    # for our possibles [952867, 357289] we can see
    # 952867 -> 0952867, 4952867; 357289 -> 0357289, 4357289, 6357289
    possibles = ["0952867", "4952867", "0357289", "4357289", "6357289"]
    # we can now narrow these down by using multipes of 3
    possibles[0] = "30952867" # 3 * 103 = 309
    del possibles[1] # no valid multipes ending in 49
    possibles[1] = "60357289" # 3 * 201 = 603
    del possibles[2] # no valid multipes ending in 43
    possibles[2] = "06357289" # 3 * 21 = 63
    # we can now take each possible and add 14 and 41 to the beginning
    possibles = ["1430952867", "4130952867", "1460357289", "4160357289", "1406357289", "4106357289"]
    answer = sum([int(x) for x in possibles])

    print(answer)

main()
