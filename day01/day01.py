from helper import *
import numpy as np

def part1(depths):
    diffs = np.diff(depths)
    num_pos = np.sum(diffs > 0, axis=0)
    print(num_pos)
    return num_pos

def part2(depths):
    window = depths[:-2] + depths[1:-1] + depths[2:]
    return part1(window)

if __name__ == '__main__':
    example = open("example.txt").read()
    input = open("input.txt").read()

    example = str_to_ints(example)
    depths = str_to_ints(input)

    assert part1(example) == 7
    part1(depths)

    assert part2(example) == 5
    part2(depths)