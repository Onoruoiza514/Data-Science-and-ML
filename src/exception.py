import sys
from src.logger import logging


def error_message_detail(error: Exception, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    return (
        f"Error occurred in Python script [{file_name}] "
        f"at line [{exc_tb.tb_lineno}] "
        f"with message [{str(error)}]"
    )


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail):
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

        # Log the full custom exception once
        logging.error(self.error_message, exc_info=True)

    def __str__(self):
        return self.error_message


