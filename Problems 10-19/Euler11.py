def main():
    # open the file and read the data
    infile = open("./Problems 10-19/problem11.txt")
    grid = infile.read().split('\n')
    for i in range(len(grid)):
        grid[i] = grid[i].split()
    # for the newline at the end of the file
    del grid[-1]

    # the largest product found
    largest = 0
    # looping over the grid checking E, S, SE, and SW
    for row in range(len(grid)):
        for num in range(len(grid[row])):
            if num < 16:
                # checking East
                prod = int(grid[row][num]) * int(grid[row][num + 1]) * int(grid[row][num + 2]) * int(grid[row][num + 3])
                if prod > largest:
                    largest = prod
                if row < 16:
                    # checking South East
                    prod = int(grid[row][num]) * int(grid[row + 1][num + 1]) * int(grid[row + 2][num + 2]) * int(grid[row + 3][num + 3])
                    if prod > largest:
                        largest = prod
            if row < 16:
                # checking South
                prod = int(grid[row][num]) * int(grid[row + 1][num]) * int(grid[row + 2][num]) * int(grid[row + 3][num])
                if prod > largest:
                    largest = prod
                if num > 2:
                    # checking South West
                    prod = int(grid[row][num]) * int(grid[row + 1][num - 1]) * int(grid[row + 2][num - 2]) * int(grid[row + 3][num - 3])
                    if prod > largest:
                        largest = prod

    infile.close()

    print(largest)

main()
