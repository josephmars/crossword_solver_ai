import networkx as nx
from constraint_graph import create_constraint_graph
from consistent import is_consistent
from heuristics import order_domain_values_simple, order_domain_values

def backtracking_search(csp):
    """
    Initiate the backtracking search algorithm.

    Args:
        csp (dict): The constraint satisfaction problem.

    Returns:
        dict or None: The assignment if successful, None otherwise.
    """
    return recursive_backtracking({}, csp)

def recursive_backtracking(assignment, csp):
    """
    Recursive function for backtracking search.

    Args:
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.

    Returns:
        dict or None: The assignment if successful, None otherwise.
    """
    if len(assignment) == len(csp):
        return assignment

    constraint_graph = create_constraint_graph(csp)
    var = select_unassigned_variable(assignment, csp, constraint_graph)

    for value in order_domain_values_simple(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            result = recursive_backtracking(assignment, csp)
            if result is not None:
                return result
            del assignment[var]
    return None

def select_unassigned_variable(assignment, csp, constraint_graph):
    """
    Select the next unassigned variable using the Minimum Remaining Values (MRV)
    and Degree heuristics.

    Args:
        assignment (dict): Current assignments of variables.
        csp (dict): The constraint satisfaction problem.
        constraint_graph (networkx.Graph): The constraint graph.

    Returns:
        str: The selected variable.
    """
    unassigned_variables = [var for var in csp if var not in assignment]

    # Sort the unassigned variables based on the number of constraints (degree) and domain size
    sorted_variables = sorted(
        unassigned_variables,
        key=lambda var: (len(csp[var]["domain"]), -len(constraint_graph[var]))
    )

    return sorted_variables[0]  # Variable with fewest choices and most constraints 