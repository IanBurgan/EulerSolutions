import datetime
# While this could be done with Gauss's algorithm, I believe this to be one
# of very few cases where learning what's behind the scenes is not worth it, and
# one should just use the library
def main():
    total = 0
    # looping the years
    for year in range(1901, 2001):
        # looping the months
        for month in range(1,13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                total += 1

    print(total)

main()
