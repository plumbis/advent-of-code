# https://adventofcode.com/2024/day/2

from itertools import pairwise

input = open("2024/inputs/02.txt", "r")

reports = []

for line in input:
    reports.append(line.split())

def compare(report: list) -> bool:

    report = list(map(int,report))
    decreasing = False
    increasing = False
    safe = True

    for i, j in pairwise(report):
        if i > j:
            decreasing = True
        if i < j:
            increasing = True
        if increasing == decreasing:
            safe = False

        if i == j:
            safe = False

        if abs(int(i) - int(j)) > 3:
            safe = False

    return safe

def part1():

    safe_count = 0


    for report in reports:
        if compare(report):
            safe_count += 1

    print(safe_count)

def part2():

    safe_count = 0

    for report in reports:
        if compare(report):
            safe_count += 1
        else:
            index = 0
            while index < len(report):
                report_copy = report.copy()
                report_copy.pop(index)
                if compare(report_copy):
                    safe_count += 1
                    break
                else:
                    index += 1

    print(safe_count)

if __name__ == "__main__":
    part1() # 463
    print("")
    part2() # 514