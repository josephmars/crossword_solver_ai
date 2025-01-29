import numpy as np
import json
import time
import matplotlib.pyplot as plt
import networkx as nx

from csp import puzzle2csp
from constraint_graph import create_constraint_graph
from backtracking import backtracking_search, select_unassigned_variable

from crossword import load_words, define_crossword_large

def main():
    # Task 2: Larger Puzzle

    # Import list of words to be used in the crossword puzzle from data/Words.txt
    words_large = load_words("data/Words.txt")
    print("Sample words loaded:", words_large[:10])

    # Define the large crossword puzzle
    crossword_large = define_crossword_large()

    # Generate CSP
    csp_large = puzzle2csp(crossword_large, words_large)
    for var in csp_large:
        print(var, csp_large[var])

    # Create constraint graph
    constraint_graph_large = create_constraint_graph(csp_large)

    # Plot the constraint graph
    fig, ax = plt.subplots(figsize=(6, 6))
    pos_large = nx.circular_layout(constraint_graph_large)
    nx.draw_networkx(
        constraint_graph_large,
        pos_large,
        with_labels=True,
        font_weight='light',
        node_color=[len(constraint_graph_large[node]) for node in constraint_graph_large],
        cmap=plt.cm.coolwarm,
        font_color='black',
        node_size=500,
        font_size=8
    )
    plt.title('Constraint Graph - Large Crossword Puzzle')
    plt.show()

    # Perform backtracking search
    start_time = time.time()
    solution_large = backtracking_search(csp_large)
    print(solution_large)
    print(f"Execution time: {time.time() - start_time} seconds")

    # Export the solution to a text file
    with open('solutions/solution_large.txt', 'w') as file:
        file.write(json.dumps(solution_large))

if __name__ == "__main__":
    main() 