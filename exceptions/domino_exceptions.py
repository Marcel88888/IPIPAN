class InvalidInputDataTypesError(Exception):
    def __init__(self):
        self.message = 'Error: Invalid input data types. Must be: (str, int:positive or 0).'
        super().__init__(self.message)


class EmptyInputStringError(Exception):
    def __init__(self):
        self.message = 'Error: Input string cannot be empty.'
        super().__init__(self.message)


class NotAllowableCharError(Exception):
    def __init__(self, given_string):
        self.__given_string = given_string
        self.__message = f'Error: Given string ("{self.__given_string}") contains illicit characters.'
        super().__init__(self.__message)


class ReverseAlgorithmNotPossibleError(Exception):
    def __init__(self, given_string):
        self.__given_string = given_string
        self.__message = fr'Error: It is not possible to create a reverse algorithm for this arrangement \
        ("{self.__given_string}"): it contains "///" or "\\\").'
        super().__init__(self.__message)
