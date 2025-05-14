import logging
from typing import List

global_logging_messages: List[str] = []


class ListHandler(logging.Handler):
    def __init__(self, log_list: List[str]):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        try:
            msg = self.format(record)
            self.log_list.append(msg)
        except Exception:
            self.handleError(record)


def setup_main_logger() -> logging.LoggerAdapter:
    logger = logging.getLogger("AutoTestFixer")
    logger.setLevel(logging.INFO)

    # Clear existing handlers to prevent duplication if called multiple times
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    # Add the custom ListHandler
    list_handler = ListHandler(global_logging_messages)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    list_handler.setFormatter(formatter)
    logger.addHandler(list_handler)

    # Optional: Add a console handler for immediate feedback during development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # If you want to use logger.domain_name or similar, you can use LoggerAdapter
    # For simplicity, we'll just return the logger for now.
    return logger


# Initialize logger when this module is imported
logger = setup_main_logger()


def get_list_handler() -> ListHandler:
    for handler_instance in logger.handlers:
        if isinstance(handler_instance, ListHandler):
            return handler_instance
    return None  # Should not happen if setup_main_logger was called
