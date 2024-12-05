# https://adventofcode.com/2024/day/4

f = open("2024/inputs/04.txt")

xword = f.read().split("\n")

def getPart1Letters(row, col):

    words = ["","","","","", "", "", ""]
    is_col_neg = False
    is_row_neg = False
    is_col_pos = False
    is_row_pos = False

    for x in range(4):
        col_neg = col - x
        row_neg = row - x

        # Prevent Arry out of bounds errors
        if col_neg < 0:
            col_neg = 0
            is_col_neg = True
        if row_neg < 0:
            row_neg = 0
            is_row_neg = True


        col_pos = col + x
        row_pos = row + x

        if col_pos > len(xword[0]) - 1:
            col_pos = len(xword[0]) - 1
            is_col_pos = True
        if row_pos > len(xword) - 1:
            row_pos = len(xword) - 1
            is_row_pos = True

        words[0] = words[0] + xword[row][col_pos]
        words[1] = words[1] + xword[row][col_neg]
        words[2] = words[2] + xword[row_pos][col]
        words[3] = words[3] + xword[row_pos][col_pos]
        words[4] = words[4] + xword[row_pos][col_neg]
        words[5] = words[5] + xword[row_neg][col]
        words[6] = words[6] + xword[row_neg][col_pos]
        words[7] = words[7] + xword[row_neg][col_neg]

    # Prevent double counting on overflow.
    # There aren't enough characters for it to match so just set it to be blank
    if is_col_neg:
        words[7] = ""
        words[4] = ""
        words[1] = ""
    if is_row_neg:
        words[5] = ""
        words[6] = ""
        words[7] = ""
    if is_col_pos:
        words[0] = ""
        words[3] = ""
        words[6] = ""
    if is_row_pos:
        words[2] = ""
        words[3] = ""
        words[4] = ""

    return words

def getPart2Letters(row, col):

    count = 0
    cross = []
    words = ["","","",""]
    is_col_neg = False
    is_row_neg = False
    is_col_pos = False
    is_row_pos = False

    for x in range(3):
        col_neg = col - x
        row_neg = row - x

        # Prevent Arry out of bounds errors
        if col_neg < 0:
            col_neg = 0
            is_col_neg = True
        if row_neg < 0:
            row_neg = 0
            is_row_neg = True


        col_pos = col + x
        row_pos = row + x

        if col_pos > len(xword[0]) - 1:
            col_pos = len(xword[0]) - 1
            is_col_pos = True
        if row_pos > len(xword) - 1:
            row_pos = len(xword) - 1
            is_row_pos = True

        # Search Down-Right
        words[0] = words[0] + xword[row_pos][col_pos]

        # Search Down-Left
        words[1] = words[1] + xword[row_pos][col_neg]

        # Search Up-Right
        words[2] = words[2] + xword[row_neg][col_pos]

        # Search Up-Left
        words[3] = words[3] + xword[row_neg][col_neg]

    # Prevent double counting on overflow.
    # There aren't enough characters for it to match so just set it to be blank
    if is_col_neg:
        words[1] = ""
        words[3] = ""
    if is_row_neg:
        words[2] = ""
        words[3] = ""
    if is_col_pos:
        words[0] = ""
        words[2] = ""
    if is_row_pos:
        words[0] = ""
        words[1] = ""


    try:
        # If Down-Right then we need to look for Up-Right
        if words[0] == "MAS":
            cross.append(xword[row + 2][col] + xword[row + 1][col + 1] + xword[row][col + 2])
        # If Down-Left then we need Up-Right
        if words[1] == "MAS":
            cross.append(xword[row + 2][col] + xword[row + 1][col - 1] + xword[row][col - 2])
        # If Up-Right then Down-Right
        if words[2] == "MAS":
            cross.append(xword[row - 2][col] + xword[row - 1][col + 1] + xword[row][col + 2])
        # If Up-Left then Down-Left
        if words[3] == "MAS":
            cross.append(xword[row - 2][col] + xword[row - 1][col - 1] + xword[row][col - 2])
    except:
        pass

    for word in cross:
        if word in ("MAS", "SAM"):
            count += 1

    return count

def part1():

    count = 0
    row = 0

    for line in xword:
        col = 0
        words = []

        for c in line:
            if c == "X":
                words.extend(getPart1Letters(row, col))
            col += 1
        row += 1

        for word in words:
            if word == "XMAS" or word == "SAMX":
                count += 1

    print(count)

def part2():

    count = 0

    row = 0

    for line in xword:
        col = 0
        sets = []

        for c in line:
            if c == "M":
                count += getPart2Letters(row, col)
            col += 1
        row += 1

    # We're counting every cross.
    # There are two crosses, so we are double counting.
    print(count/2)

part1() # 2557
part2() # 1854