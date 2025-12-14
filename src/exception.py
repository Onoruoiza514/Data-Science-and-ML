import sys
import logging

def error_message_detail(error: Exception, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = (
        f"Error occurred in Python script [{file_name}] "
        f"at line [{exc_tb.tb_lineno}] "
        f"with message [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero exception occurred.")
        raise CustomException(e, sys)
