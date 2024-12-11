# https://adventofcode.com/2024/day/6
import re

f = open("2024/inputs/06.txt")

grid = f.read().split("\n")

grid_width = len(grid[0]) - 1
grid_heigh = len(grid) - 1
verbose = False

def mark_line(line, y, x):
    grid[y] = line[:x] + "X" + line[x + 1:]

def part1():

    guard = re.compile(r"\^")
    object_re = re.compile(r"\#")
    guard_pos = []
    objects = {}
    direction = "up"

    for row, line in enumerate(grid):
        for match in re.finditer(guard, line):
            guard_pos = [row, match.start()]

        for match in re.finditer(object_re, line):
            col = match.start()
            if row in objects:
                objects[row].append(col)
            else:
                objects[row] = [col]

    moving = True
    move_count = 0
    while moving:
        if verbose:
            for line in grid:
                print(line)
            print("")

        y = guard_pos[0]
        x = guard_pos[1]
        original_line = grid[y]

        if direction == "up":
            if y - 1 < 0:
                moving = False
                mark_line(original_line, y, x)
            elif grid[y - 1][x] == "#":
                direction = "right"
                mark_line(original_line, y, x)
            else:
                mark_line(original_line, y, x)
                move_count += 1
                guard_pos[0] = y - 1
        elif direction == "right":
            if x + 1 >= len(grid[0]):
                moving = False
                mark_line(original_line, y, x)
            elif grid[y][x + 1] == "#":
                direction = "down"
                mark_line(original_line, y, x)
            else:
                mark_line(original_line, y, x)
                move_count += 1
                guard_pos[1] = x + 1
        elif direction == "down":
            if y + 1 >= len(grid[0]):
                moving = False
                mark_line(original_line, y, x)
            elif grid[y + 1][x] == "#":
                direction = "left"
                mark_line(original_line, y, x)
            else:
                mark_line(original_line, y, x)
                move_count += 1
                guard_pos[0] = y + 1
        elif direction == "left":
            if x < 0:
                moving = False
                mark_line(original_line, y, x)
            elif grid[y][x - 1] == "#":
                direction = "up"
                mark_line(original_line, y, x)
            else:
                mark_line(original_line, y, x)
                move_count += 1
                guard_pos[1] = x -1

    exes = 0
    for line in grid:
        exes += line.count("X")

    print(exes)

part1() # 4647