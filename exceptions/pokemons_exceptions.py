class InvalidInputDataTypesError(Exception):
    def __init__(self):
        self.message = 'Error: Invalid input data types. Must be: (str, list<str>).'
        super().__init__(self.message)


class EmptyInputStringError(Exception):
    def __init__(self):
        self.message = 'Error: Input strings cannot be empty.'
        super().__init__(self.message)

