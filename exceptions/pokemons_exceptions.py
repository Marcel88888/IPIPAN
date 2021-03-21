class InvalidInputDataTypesError(Exception):
    def __init__(self):
        self.message = 'Error: Invalid input data types. Must be: (str, list<str>).'
        super().__init__(self.message)


class EmptyInputStringError(Exception):
    def __init__(self):
        self.message = 'Error: Input strings cannot be empty.'
        super().__init__(self.message)


class AttackNotDefinedError(Exception):
    def __init__(self, given_type):
        self.given_type = given_type
        self.message = f'Error: Attack value not defined for "{self.given_type}" type.'
        super().__init__(self.message)

