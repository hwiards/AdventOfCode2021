import numpy as np

def read(input):
    dots = set()
    folds = []

    for line in input: #type: str
        if line.startswith("fold along"):
            ax, num = line.strip().split()[2].split("=")
            folds.append((ax, int(num)))
        elif line.strip():
            x,y = line.strip().split(',')
            dots.add((int(x),int(y)))

    return dots, folds

def part1(input):
    dots, folds = read(input)
    ax, num = folds[0]
    return len(fold(ax, num, dots))


def fold(ax, num, dots):
    return {(x - 2*(x-num), y) if x > num else (x,y) for (x,y) in dots } if ax == 'x' else \
            {(x, y - 2*(y-num)) if y > num else (x,y) for (x,y) in dots }


def part2(input):
    dots, folds = read(input)
    for ax, num in folds:
        dots = fold(ax, num, dots)
        if ax == 'x': #each fold reduces the max value in this dimension
            lastx = num
        else:
            lasty = num

    arr = np.full((lasty, lastx), '.')
    for x,y in dots:
        arr[y,x] = '#'

    np.set_printoptions(linewidth=1000) #dirty but works ;)
    print(arr)


if __name__ == '__main__':
    example = open('example.txt').readlines()
    input=open('input.txt').readlines()

    assert part1(example) == 17
    print(part1(input))
    part2(input)