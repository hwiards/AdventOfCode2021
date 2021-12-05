from collections import defaultdict, Counter

def parse(data):
    lines = []
    for line in data:
        if len(line) == 1: continue
        s, e = line.strip().split(' -> ')
        xs, ys = map(int, s.split(','))
        xe, ye = map(int, e.split(','))
        if xs > xe or ys > ye:
            xs, ys, xe, ye = xe, ye, xs, ys
        lines.append((xs, ys, xe, ye))
    return lines

def no_diags (lines:list):
    return [line for line in lines if line[0] == line[2] or line[1] == line[3]]

def part1(lines):
    points_nodiag = defaultdict(int)
    points_diag = defaultdict(int)

    for line in lines:
        xs, ys, xe, ye = line
        if xs == xe:
            for y in range(ys, ye+1):
                points_nodiag[(xs, y)] += 1
        elif ys == ye:
            for x in range(xs, xe+1):
                points_nodiag[(x, ys)] += 1
        else:
            if xs < xe and ys < ye:
                for i in range(xe-xs+1):
                    points_diag[(xs+i, ys+i)] += 1
            elif xs < xe and ys > ye:
                for i in range(xe-xs+1):
                    points_diag[(xs+i, ys-i)] += 1
            elif xs > xe and ys < ye:
                for i in range(xs-xe+1):
                    points_diag[(xs-i, ys+i)] += 1
            else:
                print(line)

    num_multi = 0
    for point, counter in points_nodiag.items():
        if counter > 1:
            num_multi += 1

    no_diag_counter = Counter(points_nodiag)
    diag_counter = Counter(points_diag)
    sum_counter = no_diag_counter + diag_counter
    sum_dict = dict(sum_counter)

    num_multi_diag = 0
    for point, counter in sum_dict.items():
        if counter > 1:
            num_multi_diag += 1

    return num_multi, num_multi_diag

def debug_map(count_dict):
    for y in range(10):
        for x in range(10):
            if (x, y) in count_dict:
                print(count_dict[(x, y)], end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    ex_input = open("example.txt").readlines()
    input = open("input.txt").readlines()

    ex_lines = parse(ex_input)
    print(part1(ex_lines))
    assert part1(ex_lines) == (5,12)

    lines = parse(input)
    print(part1(lines))
