import re

f = open("2023/inputs/03a.txt", "r", encoding="utf-8")

grid = f.read().split("\n")

def part1():

    row = 0
    part_nums = set()

    for line in grid:
        col = 0

        while col < len(line) - 1:
            start = col

            while line[col].isdigit():
                col += 1

            end = col

            # before
            try:
                if start - 1 < 0:
                    break
                check = grid[row][start - 1]
                if not check == ".":
                    part_nums.add(line[start:end])
            except:
                pass

            # after
            try:
                if end + 1 > len(line):
                    break
                check = grid[row][end + 1]
                if not check == ".":
                    part_nums.add(line[start:end])
            except:
                pass

            # down
            try:
                if row - 1 < 0:
                    break

                if end + 1 > len(line):
                    last = len(line)
                else:
                    last = end + 1

                for temp_col in range(start, last):
                    check = grid[row - 1][temp_col]
                    if not check == ".":
                        part_nums.add(line[start:end])
            except:
                pass

            # up
            try:
                if row - 1 < 0:
                    break
                if end + 1 > len(line):
                    last = len(line)
                else:
                    last = end + 1
                for temp_col in range(start,end + 1):
                    check = grid[row - 1][temp_col]
                    if not check == ".":
                        part_nums.add(line[start:end])
            except:
                pass

            col += 1

        row += 1

    for line in part_nums:
        print(line)

def part2():

    pass

if __name__ == "__main__":
    part1()