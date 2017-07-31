from collections import Counter

# not proud, but it works
def main():
    f = open('problem54.txt', 'r')

    total = 0

    for line in f:
        cards = line.split()
        pHand = toTuples(cards[:5])
        eHand = toTuples(cards[5:])

        total += comp(pHand, eHand)

    f.close()

    print(total)

def toTuples(hand):
    return ([toInt(x[0]) for x in hand], [x[1] for x in hand])

def comp(pHand, eHand):
    pHist = Counter(pHand[0]).values()
    pFlush = pHand[1].count(pHand[1][0]) == 5
    pStraight = isStraight(pHist, pHand[0])
    eHist = Counter(eHand[0]).values()
    eFlush = eHand[1].count(eHand[1][0]) == 5
    eStraight = isStraight(eHist, eHand[0])

    pSF = pStraight and pFlush
    eSF = eStraight and eFlush

    # ensure same straight flush status
    if pSF and not eSF:
        return 1
    elif not pSF and eSF:
        return 0

    # ensure same 4 of a kind status
    if max(pHist) == 4 and max(eHist) != 4:
        return 1
    elif max(pHist) != 4 and max(eHist) == 4:
        return 0

    # ensure same full house status
    if len(pHist) == 2 and len(eHist) != 2:
        return 1
    elif len(pHist) != 2 and len(eHist) == 2:
        return 0

    # ensure same flush status
    if pFlush and not eFlush:
        return 1
    elif not pFlush and eFlush:
        return 0

    # ensure same straight status
    if pStraight and not eStraight:
        return 1
    elif not pStraight and eStraight:
        return 0

    # ensure same 3 of a kind status
    if max(pHist) == 3 and max(eHist) != 3:
        return 1
    elif max(pHist) != 3 and max(eHist) == 3:
        return 0

    # ensure same boat status
    if list(pHist).count(2) == 2 and list(eHist).count(2) != 2:
        return 1
    elif list(pHist).count(2) != 2 and list(eHist).count(2) == 2:
        return 0

    # ensure same number of matches
    if max(pHist) > max(eHist):
        return 1
    elif max(pHist) < max(eHist):
        return 0

    if max(pHist) > 1:
        pNum = Counter(pHand[0]).most_common(1)[0][0]
        eNum = Counter(eHand[0]).most_common(1)[0][0]
        if pNum > eNum:
            return 1
        elif eNum > pNum:
            return 0

    # check for high card
    pDec = sorted(pHand[0], reverse=True)
    eDec = sorted(eHand[0], reverse=True)
    for i in range(len(pHand[0])):
        if pDec[i] > eDec[i]:
            return 1
        elif pDec[i] < eDec[i]:
            return 0

    raise Exception('No winner determined')


def isStraight(hist, nums):
    if max(hist) != 1:
        return False
    else:
        asc = sorted(nums)
        if asc[-1] - asc[0] == 4:
            return True
        elif asc[-1] == 14 and asc[-2] == 5:
            return True
        else:
            return False

def toInt(val):
    if val == 'A':
        return 14
    elif val == 'K':
        return 13
    elif val == 'Q':
        return 12
    elif val == 'J':
        return 11
    elif val == 'T':
        return 10
    else:
        return int(val)

main()
