import numpy as np

def solve(input):
    lenx = len(input[0].strip())
    leny = len(input)
    arr = np.zeros((leny, lenx), dtype=int)
    for y, row in enumerate(input):
        for x, digit in enumerate(row.strip()):
            arr[y, x] = digit

    flash_counter = 0
    counter = 0
    while True:
        if counter == 100:
            final_flash_counter = flash_counter
        counter += 1
        arr = arr + 1
        flash_positons = np.argwhere(arr > 9)
        for y,x in flash_positons:
            flash_counter += flash(arr, y,x)
        arr[arr > 9] = 0
        if not np.any(arr):
            break

    return final_flash_counter, counter

def flash(arr, y,x):
    flash_counter = 1
    for j,i in [(1,1), (1,0), (1,-1), (0,1), (0,-1), (-1, 1), (-1, 0), (-1,-1)]:
        if y+j >=0 and y+j <10 and x+i >=0 and x+i < 10:
            arr[y+j, x+i] += 1
            if arr[y+j, x+i] == 10:
                flash_counter += flash(arr, y+j, x+i)
    return flash_counter



if __name__ == '__main__':
    example = open('example.txt').readlines()
    input = open('input.txt').readlines()

    assert solve(example) == (1656, 195)
    print(solve(input))

