import numpy as np

dirs = [(1,0), (-1, 0), (0,1), (0,-1)]

def part1(input):
    lenx = len(input[0].strip())
    leny = len(input)
    arr = np.zeros((leny, lenx), dtype=int)
    for y, row in enumerate(input):
        for x, digit in enumerate(row.strip()):
            arr[y, x] = digit

    arr = np.pad(arr, 1, constant_values=9)

    basins = []
    risk = 0
    for j in range(1, leny + 1):
        for i in range(1, lenx + 1):
            if arr[j, i] < arr[j - 1, i] and \
                    arr[j, i] < arr[j + 1, i] and \
                    arr[j, i] < arr[j, i + 1] and \
                    arr[j, i] < arr[j, i - 1]:
                risk += arr[j, i] + 1
                basins.append({(j,i)})

    for basin in basins:
        got_bigger = True
        while got_bigger:
            got_bigger = False
            for (j,i) in basin.copy():
                for (dy, dx) in dirs:
                    if arr[j+dy, i+dx] < 9:
                        if (j+dy, i+dx) not in basin:
                            basin.add((j+dy, i+dx))
                            got_bigger = True

    basins = sorted(basins, key=len, reverse=True)
    basin_sizes = len(basins[0]) * len(basins[1]) * len(basins[2])

    return risk, basin_sizes


if __name__ == '__main__':
    example = open('example.txt').readlines()
    input = open('input.txt').readlines()

    assert part1(example) == (15, 1134)
    print(part1(input))