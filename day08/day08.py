from collections import Counter

def part1(input):
    # for line in input:
    #     output_digits = line.split(" | ")[1].strip()
    #     output_lens = list(map(len, output_digits.split()))

    output_lens = [list(map(len, l.split(" | ")[1].split())) for l in input]
    print(output_lens)
    print(Counter(output_lens))

if __name__ == '__main__':
    example = open("example.txt").readlines()
    input = open("input.txt").readlines()

    assert part1(example) == 26