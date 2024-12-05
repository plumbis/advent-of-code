# https://adventofcode.com/2024/day/3
import re

with open("2024/inputs/03.txt", "r") as file:
    input = file.read().replace("\n", "")


def part1():

    sum = 0
    nums = re.compile(r"\d{1,3}")
    expr = re.compile(r"mul\(\d{1,3}\,\d{1,3}\)")

    matches = expr.findall(input)

    for match in matches:
        a, b = nums.findall(match)
        sum += int(a) * int(b)

    print(sum)

def part2():

    sum = 0

    nums = re.compile(r"\d{1,3}")
    mul = re.compile(r"mul\(\d{1,3}\,\d{1,3}\)")

    # every mul() from the beginning to the first don't()
    first_dont = re.compile(r"mul\(\d{1,3},\d{1,3}\)(.+?)don\'t\(\)")

    # capture the contents between do() and don't()
    do_dont = re.compile(r"do\(\)(.*?)(don\'t\(\))")

    # start to first don't()
    for match in mul.findall(first_dont.search(input).group(0)):
        a, b = nums.findall(match)
        sum += int(a) * int(b)

    # get everything between every do() and don't()
    for match in do_dont.findall(input):
        # capture only the mul()
        for multiply in mul.findall(match[0]):

            # capture the numbers in the mul()
            a, b = nums.findall(multiply)
            sum += int(a) * int(b)

    print(sum)

if __name__ == "__main__":
    part1()
    print("")
    part2()