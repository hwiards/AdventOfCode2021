
def part1(input):
    legal_pairs = {
        '(' : ( ')', 1),
        '[' : ( ']', 2),
        '{' : ('}', 3),
        '<' : ('>', 4)
    }
    error_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    error = 0
    completion_points = []
    for line in input:
        broken = False
        stack = []
        completion_points_line = 0
        for char in line.strip():
            if char in legal_pairs:
                stack.append(legal_pairs[char])
            else:
                corr_elem = stack.pop()
                if char != corr_elem[1]:
                    error += error_points[char]
                    broken = True
                    break
        if not broken:
            for _, _, points in stack[::-1]:
                completion_points_line *= 5
                completion_points_line += points
            completion_points.append(completion_points_line)

    completion_points = sorted(completion_points)
    return error, completion_points[(len(completion_points)) // 2]

if __name__ == '__main__':
    example = open('example.txt').readlines()
    input = open('input.txt').readlines()

    assert part1(example) == (26397, 288957)
    print(part1(input))