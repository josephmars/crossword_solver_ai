def order_domain_values_simple(var, assignment, csp):
    """
    Order domain values using the least constraining value heuristic.

    Args:
        var (str): The variable to assign.
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        list: Ordered list of domain values.
    """
    values = csp[var]["domain"]
    
    # Remove the values that have been already assigned
    values = [value for value in values if value not in assignment.values()]
    
    # Return the values ordered by the number of conflicts, highest to lowest
    return sorted(values, key=lambda value: count_conflicts(var, value, assignment, csp), reverse=True)

def count_conflicts(var, value, assignment, csp):
    """
    Count the number of conflicts a value has with existing assignments.

    Args:
        var (str): The variable being assigned.
        value (str): The value to assign.
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        int: Number of conflicts.
    """
    conflicts = 0
    for other_var in csp:
        if other_var in assignment and other_var != var:
            other_value = assignment[other_var]
            overlap_positions = get_overlap_positions(var, other_var, csp)
            for pos in overlap_positions:
                idx_var = get_letter_index(var, pos, csp)
                idx_other = get_letter_index(other_var, pos, csp)
                if value[idx_var] != other_value[idx_other]:
                    conflicts += 1
    return conflicts

def order_domain_values(var, assignment, csp):
    """
    Order domain values using a combination of least constraining value,
    frequency heuristic, and overlap heuristic.

    Args:
        var (str): The variable to assign.
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        list: Ordered list of domain values.
    """
    values = csp[var]["domain"]

    # Remove the values that have been already assigned
    values = [value for value in values if value not in assignment.values()]

    # Sort values based on least constraining and additional heuristics
    return sorted(values, key=lambda value: (
        -frequency_heuristic(value, csp),
        -overlap_heuristic(var, value, assignment, csp)
    ))

def frequency_heuristic(word, csp):
    """
    Calculate a frequency heuristic score for a word based on letter frequency in the puzzle.

    Args:
        word (str): The word to evaluate.
        csp (dict): The constraint satisfaction problem.

    Returns:
        int: Frequency score.
    """
    puzzle_letters = [letter for var in csp for word_option in csp[var]['domain'] for letter in word_option]
    return sum(1 for letter in word if letter.lower() in [l.lower() for l in puzzle_letters])

def overlap_heuristic(var, value, assignment, csp):
    """
    Calculate an overlap heuristic score based on shared positions with assigned variables.

    Args:
        var (str): The variable being assigned.
        value (str): The value to assign.
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        int: Overlap score.
    """
    positions = get_word_positions(var, csp)
    overlap_count = sum(1 for position in positions if position in get_assigned_positions(assignment, csp))
    return overlap_count

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

def get_assigned_positions(assignment, csp):
    """
    Get all positions that have been assigned in the current assignment.

    Args:
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        set: Set of assigned positions.
    """
    positions = set()
    for var, value in assignment.items():
        direction = csp[var]["direction"]
        starting_position = csp[var]["starting_position"]
        for i in range(len(value)):
            if direction == "across":
                pos = (starting_position[0], starting_position[1] + i)
            else:
                pos = (starting_position[0] + i, starting_position[1])
            positions.add(pos)
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