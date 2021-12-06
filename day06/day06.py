from collections import defaultdict
EXAMPLE = "3,4,3,1,2"

def version1(input, days):
    fishes = [int(i) for i in input.split(",")]

    for i in range(days):
        for pos, fish in enumerate(fishes[:]):
            if fish == 0:
                fishes[pos] = 6
                fishes.append(8)
            else:
                fishes[pos] -= 1
    return len(fishes)

def version2(input, days):
    fishes = [int(i) for i in input.split(",")]
    fishes_dict = defaultdict(int)
    for fish in fishes:
        fishes_dict[fish] += 1

    for _ in range(days):
        temp_dict = defaultdict(int)
        for day, num in fishes_dict.items():
            if day == 0:
                temp_dict[6] += num
                temp_dict[8] += num
            else:
                temp_dict[day-1] += num
        fishes_dict = temp_dict

    return sum(fishes_dict.values())


if __name__ == '__main__':
    input = open("input.txt").readline()

    assert version1(EXAMPLE, 80) == 5934
    print(version1(input, 80))

    # The first version does not scale ;)
    assert version2(EXAMPLE, 256) == 26984457539
    print(version2(input, 256))