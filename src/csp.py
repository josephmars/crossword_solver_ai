import numpy as np

def puzzle2csp(crossword, words, del_list=[], prior_knowledge={}):
    """
    Converts a crossword puzzle into a CSP problem.

    Args:
        crossword (np.array): The crossword puzzle grid.
        words (list): List of possible words.
        del_list (list, optional): Variables to be deleted from the CSP.
        prior_knowledge (dict, optional): Pre-assigned values for certain variables.

    Returns:
        dict: A dictionary representing the CSP with variables and their domains.
    """
    domains = {}
    # Add domains to the list for each word in the crossword puzzle
    for row in range(crossword.shape[0]):
        for col in range(crossword.shape[1]):
            if crossword[row][col] > 0:
                # Check if the word is across
                if col + 1 < crossword.shape[1] and crossword[row][col + 1] >= 0:
                    # Determine the length of the word
                    word_length = 1
                    for i in range(col + 1, crossword.shape[1]):
                        if crossword[row][i] >= 0:
                            word_length += 1
                        else:
                            break

                    # Obtain the domain 
                    domain = [word for word in words if len(word) == word_length]
                    # Sort the domain by the number of vowels in the word
                    domain = sorted(domain, key=lambda value: sum([1 for letter in value if letter.lower() in "aeiou"]), reverse=True)

                    # Add the domain to the list if it is not empty:
                    if len(domain) > 0:
                        var_name = f"{crossword[row][col]}across"
                        domains[var_name] = {
                            "starting_position": (row, col),
                            "length": word_length,
                            "direction": "across",
                            "domain": domain
                        }

                # Check if the word is down
                if row + 1 < crossword.shape[0] and crossword[row + 1][col] >= 0:
                    # Determine the length of the word
                    word_length = 1
                    for i in range(row + 1, crossword.shape[0]):
                        if crossword[i][col] >= 0:
                            word_length += 1
                        else:
                            break

                    # Obtain the domain 
                    domain = [word for word in words if len(word) == word_length]

                    # Add the domain to the list if it is not empty:
                    if len(domain) > 0:
                        var_name = f"{crossword[row][col]}down"
                        domains[var_name] = {
                            "starting_position": (row, col),
                            "length": word_length,
                            "direction": "down",
                            "domain": domain
                        }

    # Remove the variables that are not in the crossword puzzle
    for var in del_list:
        if var in domains:
            del domains[var]

    # Add prior knowledge to the domains
    for var, values in prior_knowledge.items():
        if var in domains:
            domains[var]["domain"] = values

    return domains 