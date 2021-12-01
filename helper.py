import numpy as np

def str_to_ints(input: str) -> np.array:
    return np.array([int(num) for num in input.split()])