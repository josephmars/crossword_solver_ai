import json

def export_solution(solution, filepath):
    """
    Export the solution dictionary to a JSON file.

    Args:
        solution (dict): The solution to export.
        filepath (str): Path to the output file.
    """
    with open(filepath, 'w') as file:
        file.write(json.dumps(solution)) 