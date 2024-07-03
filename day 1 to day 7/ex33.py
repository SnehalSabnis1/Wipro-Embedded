import logging
logging.basicConfig(level=logging.DEBUG,filename='messages.log',filemode='w')
logger=logging.getLogger()

logger.debug("this is a debug log")
logger.info("this is a information log")
logger.warning("this is a warning log")
logger.critical("this is critical log")