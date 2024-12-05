# https://adventofcode.com/2024/day/1

input = open("2024/inputs/01.txt", "r")

col1 = []
col2 = []

for line in input:
    cols = line.split()
    col1.append(cols[0])
    col2.append(cols[1])

def part1():
    col1.sort()
    col2.sort()
    result = 0

    for count, elem in enumerate(col1):
        result += abs(int(elem) - int(col2[count]))

    print(result)

def part2():

    sum = 0

    for num in col1:
        count = col2.count(num)
        sum += (count * int(num))

    print(sum)


if __name__ == "__main__":
    # part1()
    part2()