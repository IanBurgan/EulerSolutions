def main():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    # 1 way to make 0 coins at first and 0 ways to make any more than 0
    ways = [1] + [0] * target

    for coin in coins:
        # starts at coin because no amount less than the coin can be changed by
        # using the coin.
        for i in range(coin, target + 1):
            # each amount can now be made by using the coin and any one of the
            # ways to make the (amount - the coin)
            ways[i] += ways[i - coin]
    print(ways[-1])

main()
