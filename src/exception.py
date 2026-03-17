"""
Custom Exception Handling Module
Author: Emmanuel Junior
Description: Centralized custom exceptions for cleaner error handling
"""

import sys
import traceback


class CustomException(Exception):
    """
    Base custom exception class that captures detailed error information
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error(error_message, error_detail)

    def get_detailed_error(self, error_message, error_detail: sys):
        """
        Extracts detailed error info including file name and line number
        """
        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno

        return f"""
Error occurred in script: {file_name}
Line number: {line_number}
Error message: {error_message}
"""

    def __str__(self):
        return self.error_message