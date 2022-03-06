import logging


# 
# 
# #logging.basicConfig(level=logging.DEBUG)
# #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# 
# # 
# logger = logging.getLogger('server_logger')
# 
# logger.setLevel(logging.DEBUG)
# # create file handler which logs even debug messages
# fh = logging.FileHandler('server.log')
# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# # create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# # add the handlers to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
# 
# 
# 
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')
# 
# 
# 
# 
# 
# logname = 'test.log'
# 
# 
# logging.basicConfig(filename=logname,
#                             filemode='a',
#                             format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                             datefmt='%H:%M:%S',
#                             level=logging.DEBUG)
# 
# logging.info("Running Urban Planning")
# 
# # self.logger = logging.getLogger('urbanGUI')
# 
# 
# 
# logging.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')




def getNewLogger(serviceName):
    # Create new logger object
    logger = logging.getLogger('server_logger')

    logger.setLevel(logging.DEBUG)
    # Create file handler which logs even debug messages
    fh = logging.FileHandler(serviceName + '.log')
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger









