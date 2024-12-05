# https://adventofcode.com/2023/day/3
import re

f = open("2023/inputs/03.txt", "r", encoding="utf-8")
grid = f.read().split("\n")

grid_height = len(grid)
grid_width = len(grid[0])

def isSym(c):
    if c == "." or c.isdigit():
        return False
    else:
        return True

def isPart(row, col_span):

    # Check Before
    if col_span[0] - 1 >= 0:
        if isSym(grid[row][col_span[0] - 1]):
            return True

    # Check After
    if col_span[1] < grid_width:
        if isSym(grid[row][col_span[1]]):
            return True

    # Check Below
    if row + 1 < grid_width:
        for c in range(col_span[0], col_span[1]):
            if isSym(grid[row + 1][c]):
                return True

        # Check bottom right
        if col_span[1] + 1 < grid_width:
            if isSym(grid[row + 1][col_span[1]]):
                return True

        # Check bottom left
        if col_span[0] - 1 >= 0:
            if isSym(grid[row + 1][col_span[0] - 1]):
                return True

    # Check Above
    if row - 1 >= 0:
        for c in range(col_span[0], col_span[1]):
            if isSym(grid[row - 1][c]):
                return True

        # Check above right
        if col_span[1] + 1 < grid_width:
            if isSym(grid[row - 1][col_span[1]]):
                return True

        # Check above left
        if col_span[0] - 1 >= 0:
            if isSym(grid[row - 1][col_span[0]- 1]):
                return True

    return False

def part1():

    row = 0
    nums = []
    digit_regex = re.compile(r"\d{1,3}")

    for line in grid:
        for match in re.finditer(digit_regex, line):
            if match.group(0) == "617":
                pass
            if isPart(row, match.span()):
                nums.append(match.group(0))
        row += 1

    print(sum(map(int,nums)))

def part2():

    pass

if __name__ == "__main__":
    part1()