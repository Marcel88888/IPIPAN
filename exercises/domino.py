from exceptions import domino_exceptions


def check_input(arrangement, iterations):
    """
    Checks if the given parameters are correct.
    :param str arrangement: starting arrangement of dominoes
    :param int iterations: number of iterations to perform
    :raise:
        domino_exceptions.InvalidInputDataTypesError if 'arrangement' is not a str or 'iterations' is not an int or
    iterations is negative
        domino_exceptions.EmptyInputStringError if 'arrangement' is an empty string
        domino_exceptions.NotAllowableCharError if 'arrangement' contains illicit characters
    """
    allowable_chars = ['|', '/', '\\']
    if not isinstance(arrangement, str) or not isinstance(iterations, int) or iterations < 0:
        raise domino_exceptions.InvalidInputDataTypesError()
    if not arrangement:
        raise domino_exceptions.EmptyInputStringError()
    if any([char not in allowable_chars for char in arrangement]):  # checking if 'arrangement' contains
        # only allowable characters.
        raise domino_exceptions.NotAllowableCharError(arrangement)


def move_domino(arrangement, iterations):
    """
    The function returns a string representing the arrangement of dominoes over a given number of iterations.
    Dominoes are represented in the form of a string, which consists of the following characters:
    '|' - the domino is intact
    '/' - the domino falls to the right
    '\' - the domino falls to the left
    :param str arrangement: starting arrangement of dominoes
    :param int iterations: number of iterations to perform
    :return str: final arrangement of the domino
    """
    check_input(arrangement, iterations)
    arrangement_list = list(arrangement)
    arr_list_bef_iter = arrangement_list.copy()  # 'arrangement list before iteration' - to avoid checking
    # some arrangements after changes during one iteration
    
    for iteration in range(iterations):
        for position, domino in enumerate(arrangement_list):
            if domino == '|':
                if 0 < position < len(arrangement_list) - 1:
                    if arr_list_bef_iter[position-1] == '/' and arr_list_bef_iter[position+1] != '\\':
                        arrangement_list[position] = '/'
                    elif arr_list_bef_iter[position-1] != '/' and arr_list_bef_iter[position+1] == '\\':
                        arrangement_list[position] = '\\'
                elif position == 0:
                    if arr_list_bef_iter[position+1] == '\\':
                        arrangement_list[position] = '\\'
                elif position == len(arrangement_list) - 1:
                    if arr_list_bef_iter[position-1] == '/':
                        arrangement_list[position] = '/'
        arr_list_bef_iter = arrangement_list.copy()
        
    return "".join(arrangement_list)


def move_domino_back(arrangement, iterations):
    """
    The function performs reverse domino movement.
    :param str arrangement: starting arrangement of dominoes
    :param int iterations: number of iterations to perform
    :raise: domino_exceptions.ReverseAlgorithmNotPossibleError if the arrangement contains at least three '/' or '\'
    characters next to each other ('///' or '\\\' at least)
    :return str: arrangement of the domino before given number of iterations
    """
    check_input(arrangement, iterations)
    if '///' in arrangement or '\\\\\\' in arrangement:
        raise domino_exceptions.ReverseAlgorithmNotPossibleError(arrangement)
    arrangement_list = list(arrangement)
    arr_list_bef_iter = arrangement_list.copy()  # 'arrangement list before iteration' - to avoid checking
    # some arrangements after changes during one iteration
    
    for iteration in range(iterations):
        for position, domino in enumerate(arrangement_list):
            if 0 < position < len(arrangement_list) - 1:
                if domino == '/' and arr_list_bef_iter[position-1] == '/' and arr_list_bef_iter[position+1] != '\\':
                    arrangement_list[position] = '|'
                elif domino == '\\' and arr_list_bef_iter[position-1] != '/' and arr_list_bef_iter[position+1] == '\\':
                    arrangement_list[position] = '|'
            elif position == 0:
                if domino == '\\' and arr_list_bef_iter[position+1] == '\\':
                    arrangement_list[position] = '|'
            elif position == len(arrangement_list) - 1:
                if domino == '/' and arr_list_bef_iter[position-1] == '/':
                    arrangement_list[position] = '|'
        arr_list_bef_iter = arrangement_list.copy()
        
    return "".join(arrangement_list)
