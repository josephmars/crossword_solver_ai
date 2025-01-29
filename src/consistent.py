def is_consistent(var, value, assignment, csp):
    """
    Check if assigning a value to a variable is consistent with the current assignment.

    Args:
        var (str): The variable to assign.
        value (str): The value to assign to the variable.
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        bool: True if consistent, False otherwise.
    """
    for other_var in assignment:
        if other_var != var:
            other_value = assignment[other_var]
            # Get overlapping positions
            overlap_positions = get_overlap_positions(var, other_var, csp)
            for pos in overlap_positions:
                idx_var = get_letter_index(var, pos, csp)
                idx_other = get_letter_index(other_var, pos, csp)
                if value[idx_var] != other_value[idx_other]:
                    return False
    return True

def get_overlap_positions(var1, var2, csp):
    """
    Get overlapping positions between two variables.

    Args:
        var1 (str): First variable.
        var2 (str): Second variable.
        csp (dict): The constraint satisfaction problem.

    Returns:
        list: List of overlapping positions.
    """
    positions1 = set(get_word_positions(var1, csp))
    positions2 = set(get_word_positions(var2, csp))
    return list(positions1 & positions2)

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

def get_letter_index(var, position, csp):
    """
    Get the index of the letter in the word corresponding to the given position.

    Args:
        var (str): The variable name.
        position (tuple): The position in the grid.
        csp (dict): The constraint satisfaction problem.

    Returns:
        int: The index of the letter in the word.
    """
    direction = csp[var]["direction"]
    starting_position = csp[var]["starting_position"]
    if direction == "across":
        return position[1] - starting_position[1]
    else:
        return position[0] - starting_position[0] 