from exceptions import domino_exceptions


def move_domino(arrangement, iterations):
    allowable_chars = ['|', '/', '\\']
    if isinstance(arrangement, str) and isinstance(iterations, int) and iterations >= 0:
        if arrangement != '':
            if all([char in allowable_chars for char in arrangement]):  # checking if 'arrangement' contains
                # only allowable characters.
                arrangement_list = list(arrangement)
                arr_list_bef_iter = arrangement_list.copy()  # 'arrangement list before iteration' - to avoid checking
                # some arrangements after changes during one iteration
                for iteration in range(iterations):
                    for position, domino in enumerate(arrangement_list):
                        if domino == '|':
                            if 0 < position < len(arrangement_list) - 1:
                                if arr_list_bef_iter[position-1] == '/' and arr_list_bef_iter[position+1] != '\\':
                                    arrangement_list[position] = '/'
                                elif arr_list_bef_iter[position+1] == '\\' and arr_list_bef_iter[position-1] != '/':
                                    arrangement_list[position] = '\\'
                            elif position == 0:
                                if arr_list_bef_iter[position+1] == '\\':
                                    arrangement_list[position] = '\\'
                            elif position == len(arrangement_list) - 1:
                                if arr_list_bef_iter[position-1] == '/':
                                    arrangement_list[position] = '/'
                    arr_list_bef_iter = arrangement_list.copy()
                return "".join(arrangement_list)
            raise domino_exceptions.NotAllowableCharError(arrangement)
        raise domino_exceptions.EmptyInputStringError()
    raise domino_exceptions.InvalidInputDataTypesError()
