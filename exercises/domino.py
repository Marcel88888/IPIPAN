from exceptions import domino_exceptions


def check_input(arrangement, iterations):
    allowable_chars = ['|', '/', '\\']
    if not isinstance(arrangement, str) or not isinstance(iterations, int) or iterations < 0:
        raise domino_exceptions.InvalidInputDataTypesError()
    if not arrangement:
        raise domino_exceptions.EmptyInputStringError()
    if any([char not in allowable_chars for char in arrangement]):  # checking if 'arrangement' contains
        # only allowable characters.
        raise domino_exceptions.NotAllowableCharError(arrangement)


def move_domino(arrangement, iterations):
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
