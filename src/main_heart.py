import numpy as np
import json
import time
import matplotlib.pyplot as plt
import networkx as nx

from csp import puzzle2csp
from constraint_graph import create_constraint_graph
from backtracking import backtracking_search

from crossword import load_words, define_crossword_heart

def main():
    # Task 2.2: Heart Puzzle

    # Define the heart-shaped crossword puzzle
    crossword_heart = define_crossword_heart()

    # Import list of words to be used in the crossword puzzle from data/Words.txt
    words_large = load_words("data/Words.txt")

    # Add prior knowledge: '34across' is assigned "jms"
    prior_knowledge = {"34across": ["JMS"]}

    # Generate CSP with prior knowledge
    csp_heart = puzzle2csp(crossword_heart, words_large, prior_knowledge=prior_knowledge)
    for var in csp_heart:
        print(var, csp_heart[var])

    # Create constraint graph
    constraint_graph_heart = create_constraint_graph(csp_heart)

    # Plot the constraint graph
    fig, ax = plt.subplots(figsize=(14, 14))
    pos_heart = nx.circular_layout(constraint_graph_heart)
    nx.draw_networkx(
        constraint_graph_heart,
        pos_heart,
        with_labels=True,
        font_weight='light',
        node_color=[len(constraint_graph_heart[node]) for node in constraint_graph_heart],
        cmap=plt.cm.coolwarm,
        font_color='black',
        node_size=500,
        font_size=8
    )
    plt.title('Constraint Graph - Heart Crossword Puzzle')
    plt.show()

    # Perform backtracking search
    start_time = time.time()
    solution_heart = backtracking_search(csp_heart)
    print(solution_heart)
    print(f"Execution time: {time.time() - start_time} seconds")

    # Export the solution to a text file
    with open('solutions/solution_heart.txt', 'w') as file:
        file.write(json.dumps(solution_heart))

if __name__ == "__main__":
    main() 