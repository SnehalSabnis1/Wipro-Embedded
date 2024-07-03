import logging
logger = logging.getLogger('sample-logger')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

fh = logging.FileHandler('messages1.log',mode='w')
fh.setLevel(logging.DEBUG)

format = logging.Formatter("%(name)s %(levelname)s %(asctime)s %(message)s")

sh.setFormatter(format)
fh.setFormatter(format)

logger.addHandler(sh)
logger.addHandler(fh)

logger.debug("this is a debug log")
logger.info("this is a information log")
logger.warning("this is a warning log")
logger.critical("this is critical log")