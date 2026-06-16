from Logger import Logger

logger = Logger().get_logger()

logger.info(1, "This is an info message.")
logger.error(2, "This is an error message.")
logger.debug(3, "This is a debug message.")
