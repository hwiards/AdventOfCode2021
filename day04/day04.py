import numpy as np

def readInput(input_file_str):
    with open(input_file_str, 'r') as input_file:
        lines = input_file.read().splitlines()
        draws = [int(i) for i in lines[0].split(',')]

        boards = []
        for start in range(2, len(lines), 6):
            board = []
            for i in range(start, start+5):
                board.append([int(j) for j in lines[i].strip().split()])
            boards.append(np.array(board))
        return draws, boards

def checkBoard(board, drawnNumbers):
    check = np.isin(board, drawnNumbers)
    if np.all(check, axis=0).any() or np.all(check, axis=1).any():
        sum = np.sum(board, where=np.invert(check))
        return sum*drawnNumbers[-1]

def part1(draws, boards):
    for i in range(len(draws)):
        for board in boards:
            is_bingo= checkBoard(board, draws[:i+1])
            if is_bingo:
                return is_bingo


def part2(draws, boards):
    for i in range(len(draws)):
        for num, board in enumerate(boards):
            is_bingo= checkBoard(board, draws[:i+1])
            if is_bingo:
                if len(boards) == 1:
                    return is_bingo
                boards.pop(num)

if __name__ == '__main__':
    ex_draws, ex_boards = readInput("example.txt")
    assert part1(ex_draws, ex_boards.copy()) == 4512
    assert part2(ex_draws, ex_boards.copy()) == 1924

    draws, boards = readInput("input.txt")
    print(part1(draws, boards))
    print(part2(draws, boards))