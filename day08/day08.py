from collections import Counter
from collections import defaultdict

def part1(input):
    output_lens = [len(output) for l in input for output in l.split(" | ")[1].split()]
    len_counter = Counter(output_lens)

    return len_counter[2] + len_counter[4] + len_counter[3] + len_counter[7]

def part2(input):
    output_value_sum = 0
    for line in input:
        nums = [set(output) for output in line.split(" | ")[0].split()]
        outputs = [frozenset(output) for output in line.split(" | ")[1].split()]
        len_dict = defaultdict(list)
        for num in nums:
            len_dict[len(num)].append(num)

        n1 = len_dict[2][0]
        n4 = len_dict[4][0]
        n7 = len_dict[3][0]
        n8 = len_dict[7][0]

        #a = set(len_dict[3][0]).difference(set(len_dict[2][0])).pop()
        for num in len_dict[6]:
            if len(num.difference(n4.union(n7))) == 1:
                g = num.difference(n4.union(n7)).pop()
                n9 = num
                e = n8.difference(n9).pop()
        for num in len_dict[5]:
            if e in num:
                n2 = num
                f = n1.difference(n2).pop()
                c = n1.difference(f).pop()
                n6 = n8.difference(c)
                n5 = n6.difference(e)
                n3 = n2.difference(e).union(f)
                d = n3.difference(n7).difference(g).pop()
                n0 = n8.difference(d)
                len_dict[5].remove(num)

        numbers = {}
        for number, keyset in enumerate([n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]):
            numbers[frozenset(keyset)] = number

        output_value = 0
        for output in outputs:
            output_value *= 10
            output_value += numbers[output]
        output_value_sum += output_value

    return output_value_sum



if __name__ == '__main__':
    example = open("example.txt").readlines()
    input = open("input.txt").readlines()

    assert part1(example) == 26
    print(part1(input))

    assert part2(example) == 61229
    print(part2(input))