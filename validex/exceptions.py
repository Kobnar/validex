class ValidexError(Exception):
    """
    A general exception class for `validex`.
    """

    DEFAULT_MESSAGE = 'An exception occurred.'

    def __init__(self, message=None):
        self.message = message or self.DEFAULT_MESSAGE

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.message)


class ValidationError(ValidexError):
    """
    A custom exception class to be thrown when data fails validation.
    """

    DEFAULT_MESSAGE = 'Validation failed.'

    def __init__(self, message=None, original_error=None):
        super().__init__(message)
        self.original_error = original_error
