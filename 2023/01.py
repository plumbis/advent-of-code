import re

def part1():
    f = open("inputs/01.txt", "r")

    global_num_set = []

    for line in f:

        line_nums = []

        for char in line:

            try:
                int(char)
            except ValueError:
                continue

            if len(line_nums) == 2:
                line_nums[1] = char
            else:
                line_nums.append(char)

        if len(line_nums) == 1:
            line_nums.append(line_nums[0])

        global_num_set.append(int("".join(line_nums)))

    print(sum(global_num_set))

def part2():

    number_strings = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
    }

    num_letters = set()
    for val in number_strings:
        num_letters.add(val[:1])

    f = open("inputs/01.txt", "r", encoding="utf-8")
    global_nums = []
    expr = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")

    for line in f:
        matches = expr.findall(line)

        if len(matches) > 0:
            if matches[0] in number_strings:
                num = number_strings[matches[0]]
            else:
                num = matches[0]

            if len(matches) == 1:
                num = num + num
            else:
                last_match = matches[len(matches) - 1]

                if last_match in number_strings:
                    num = num + number_strings[last_match]
                else:
                    num = num + last_match

            print(num)
            global_nums.append(int(num))

    print(sum(global_nums))


if __name__ == "__main__":
    part1()
    part2()