import numpy as np

def load_words(filepath):
    """
    Load words from a text file.

    Args:
        filepath (str): Path to the words file.

    Returns:
        list: List of words.
    """
    words = []
    with open(filepath, "r") as f:
        for line in f:
            words.append(line.strip())
    return words

def define_crossword_small():
    """
    Define the small crossword puzzle.

    Returns:
        np.array: The small crossword grid.
    """
    return np.array([
        [1, 0, 2, 0, 3],
        [-1, -1, 0, -1, 0],
        [-1, 4, 0, 5, 0],
        [6, -1, 7, 0, 0],
        [8, 0, 0, 0, 0],
        [0, -1, -1, 0, -1]
    ])

def define_crossword_large():
    """
    Define the large crossword puzzle.

    Returns:
        np.array: The large crossword grid.
    """
    return np.array([
        [-1,-1,1,0,0,0,0,0,2,-1,-1,-1],
        [-1,-1,0,-1,-1,-1,-1,-1,0,-1,-1,3],
        [-1,-1,0,-1,-1,-1,-1,-1,0,-1,-1,0],
        [-1,-1,0,-1,-1,4,0,5,0,0,-1,0],
        [-1,-1,0,-1,-1,-1,-1,0,-1,-1,-1,0],
        [-1,-1,-1,-1,6,-1,-1,7,0,8,0,0],
        [-1,-1,-1,-1,0,-1,-1,0,-1,0,-1,0],
        [-1,9,-1,10,0,0,0,0,-1,0,-1,-1],
        [-1,0,-1,-1,0,-1,-1,0,-1,0,-1,-1],
        [11,0,0,0,0,0,-1,-1,-1,0,-1,-1],
        [-1,0,-1,-1,0,-1,-1,-1,-1,0,-1,-1]
    ])

def define_crossword_heart():
    """
    Define the heart-shaped crossword puzzle.

    Returns:
        np.array: The heart crossword grid.
    """
    return np.array([
        [-1,-1,1,2,3,-1,-1,-1,4,5,6,-1,-1],
        [-1,7,0,0,0,8,-1,9,0,0,0,10,-1],
        [-1,11,0,0,0,0,-1,12,0,0,0,0,-1],
        [13,0,0,-1,14,0,15,0,0,-1,16,0,17],
        [18,0,0,19,-1,20,0,0,-1,21,0,0,0],
        [22,0,0,0,-1,23,0,0,-1,24,0,0,0],
        [-1,25,0,0,26,-1,-1,-1,27,0,0,0,-1],
        [-1,-1,28,0,0,29,-1,30,0,0,0,-1,-1],
        [-1,-1,-1,31,0,0,32,0,0,0,-1,-1,-1],
        [-1,-1,-1,-1,33,0,0,0,0,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,34,0,0,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,0,-1,-1,-1,-1,-1,-1]
    ]) 