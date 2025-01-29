import networkx as nx

def create_constraint_graph(csp):
    """
    Create a constraint graph from the given CSP.

    Args:
        csp (dict): The constraint satisfaction problem.

    Returns:
        networkx.Graph: The constraint graph.
    """
    constraint_graph = nx.Graph()

    # Add nodes for each variable
    constraint_graph.add_nodes_from(csp.keys())

    # Add edges for conflicts between variables
    for var1 in csp:
        for var2 in csp:
            if var1 != var2:
                if conflicts_exist(var1, var2, csp):
                    constraint_graph.add_edge(var1, var2)

    return constraint_graph

def conflicts_exist(var1, var2, csp):
    """
    Check if conflicts exist between two variables.

    Args:
        var1 (str): First variable.
        var2 (str): Second variable.
        csp (dict): The constraint satisfaction problem.

    Returns:
        bool: True if a conflict exists, False otherwise.
    """
    for position1 in get_word_positions(var1, csp):
        for position2 in get_word_positions(var2, csp):
            if position1 == position2:
                return True
    return False

def get_word_positions(var, csp):
    """
    Get the matrix positions of a word variable.

    Args:
        var (str): The variable name.
        csp (dict): The constraint satisfaction problem.

    Returns:
        list: List of positions occupied by the word.
    """
    positions = []
    direction = csp[var]["direction"]
    starting_position = csp[var]["starting_position"]
    length = csp[var]["length"]

    for i in range(length):
        if direction == "across":
            positions.append((starting_position[0], starting_position[1] + i))
        else:
            positions.append((starting_position[0] + i, starting_position[1]))

    return positions 