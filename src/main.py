from logger import logger

if __name__ == "__main__":
    logger.debug("This is a debug message (logged to file).")
    logger.info("This is an info message (logged to file and Graylog).")
    logger.warning("This is a warning message (logged to file, console, and Graylog).")
    logger.error("This is an error message (logged to all).")
    logger.critical("This is a critical message (logged to all).")
