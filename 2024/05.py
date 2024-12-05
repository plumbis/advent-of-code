# https://adventofcode.com/2024/day/5

f = open("2024/inputs/05.txt")

page_order = {}
reports = []

def load_reports():
    for line in f:
        line = line.replace("\n", "")
        if "|" in line:
            pages = tuple(line.split("|"))
            key = pages[0]
            if key in page_order:
                page_order[key].append(pages[1])
            else:
                page_order[key] = [pages[1]]
        elif "," in line:
            reports.append(line.split(","))

def part1():
    middles = []
    bad_reports = []
    for report in reports:
        good_report = True

        for val in report:
            if val in page_order:
                for page in page_order[val]:
                    if page in report:
                        if report.index(page) < report.index(val):
                            good_report = False

        if good_report:
            middles.append(report[int(len(report)/2)])
        else:
            bad_reports.append(report)

    print(sum(map(int,middles)))
    return bad_reports

def part2(bad_reports):
    middles = []
    all_clear = True
    runs = 0

    while not all_clear or runs == 0:
        if runs > 0:
            all_clear = True
        for report in bad_reports:
            for val in report:
                if val in page_order:
                    for page in page_order[val]:
                        if page in report:
                            page_index = report.index(page)
                            val_index = report.index(val)
                            if page_index < val_index:
                                report[page_index], report[val_index] = report[val_index], report[page_index]
                                all_clear = False

        runs += 1

    for report in bad_reports:
        middles.append(report[int(len(report)/2)])

    print(sum(map(int,middles)))


load_reports()
bad_reports = part1() # 7303
print("")
part2(bad_reports) # 4713
