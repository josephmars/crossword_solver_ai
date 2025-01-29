import numpy as np
import json
import time
import matplotlib.pyplot as plt
import networkx as nx

from csp import puzzle2csp
from constraint_graph import create_constraint_graph
from backtracking import backtracking_search

def main():
    # Task 1: Backtracking (30 pts)

    # Create a list of words to be used in the crossword puzzle
    words_small = ["AFT","LASER","ALE","LEE","EEL","LINE","HEEL","SAILS","HIKE","SHEET","HOSES","STEER","KEEL","TIE","KNOT"]

    # Define the small crossword puzzle
    crossword_small = np.array([
        [1, 0, 2, 0, 3],
        [-1, -1, 0, -1, 0],
        [-1, 4, 0, 5, 0],
        [6, -1, 7, 0, 0],
        [8, 0, 0, 0, 0],
        [0, -1, -1, 0, -1]
    ])

    # Generate CSP
    csp_small = puzzle2csp(crossword_small, words_small, del_list=["2across"])
    for var in csp_small:
        print(var, csp_small[var])

    # Create constraint graph
    constraint_graph_small = create_constraint_graph(csp_small)

    # Plot the constraint graph
    fig, ax = plt.subplots(figsize=(5, 5))
    pos_small = nx.circular_layout(constraint_graph_small)
    nx.draw_networkx(
        constraint_graph_small,
        pos_small,
        with_labels=True,
        font_weight='light',
        node_color=[len(constraint_graph_small[node]) for node in constraint_graph_small],
        cmap=plt.cm.coolwarm,
        font_color='black',
        node_size=500,
        font_size=8
    )
    plt.title('Constraint Graph - Small Crossword Puzzle')
    plt.show()

    # Perform backtracking search
    start_time = time.time()
    solution = backtracking_search(csp_small)
    print(solution)
    print(f"Execution time: {time.time() - start_time} seconds")

    # Export the solution to a text file
    with open('solutions/solution_small.txt', 'w') as file:
        file.write(json.dumps(solution))

if __name__ == "__main__":
    main() 