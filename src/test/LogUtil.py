import logging




def getNewLogger(serviceName):
    # Create new logger object
    logger = logging.getLogger('server_logger')

    logger.setLevel(logging.DEBUG)
    # Create file handler which logs even debug messages
    fh = logging.FileHandler(serviceName + '.log')
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    #ch.setLevel(logging.ERROR)
    ch.setLevel(logging.DEBUG)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger









