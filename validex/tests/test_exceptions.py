import unittest


class ValidexErrorTests(unittest.TestCase):

    def test_default_message_set(self):
        """ValidexError sets a default message if no custom message is defined
        """
        from ..exceptions import ValidexError
        error = ValidexError()
        self.assertEqual(ValidexError.DEFAULT_MESSAGE, error.message)

    def test_custom_message_set(self):
        """ValidexError sets a custom message if one is defined
        """
        from ..exceptions import ValidexError
        err_msg = 'Something went wrong.'
        error = ValidexError(err_msg)
        self.assertEqual(err_msg, error.message)

    def test_str_includes_error_name(self):
        """ValidexError.__str__() includes its own name
        """
        from ..exceptions import ValidexError
        error = ValidexError()
        err_str = str(error)
        self.assertTrue(err_str.startswith('ValidexError: '))

    def test_str_includes_default_message(self):
        """ValidexError.__str__() includes a default error message if one is not defined
        """
        from ..exceptions import ValidexError
        error = ValidexError()
        err_str = str(error)
        self.assertTrue(err_str.endswith(ValidexError.DEFAULT_MESSAGE))

    def test_str_includes_custom_message(self):
        """ValidexError.__str__() includes a custom error message if one is defined
        """
        from ..exceptions import ValidexError
        err_msg = 'Something went wrong.'
        error = ValidexError(err_msg)
        err_str = str(error)
        self.assertTrue(err_str.endswith(err_msg))


class ValidationErrorTests(unittest.TestCase):

    def test_default_message_set(self):
        """ValidexError sets a default message if no custom message is defined
        """
        from ..exceptions import ValidationError
        error = ValidationError()
        self.assertEqual(ValidationError.DEFAULT_MESSAGE, error.message)

    def test_original_error_set(self):
        """ValidationError sets an "original error" if one is defined
        """
        from ..exceptions import ValidationError
        orig_err = KeyError()
        error = ValidationError(original_error=orig_err)
        self.assertEqual(orig_err, error.original_error)
