import logging


def getlogger():
    filename ="C:\\HU Training\\Embedded Systems\\EmbeddedTestingMockAPI\\Log\\Logfile.log"
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(filename, 'w')
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
