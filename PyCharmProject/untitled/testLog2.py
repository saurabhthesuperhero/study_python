import logging
from logging import handlers

# formatter setting
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# timedRotatingFileHandler setting
logHandler = handlers.TimedRotatingFileHandler(filename='rotatinglog.log', when='S', interval=5, encoding='utf-8')
logHandler.setFormatter(formatter)
logHandler.prefix = '%Y%m%d'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logHandler)

logger.debug('start log')

def factorial(n):
    logging.debug('start factorial(%s)' % (n) )
    total = 1
    for i in range(n + 1):
        if not i:
            continue
        total *= i
        logging.debug('i is %s, total is %s' % (i, total) )
    logging.debug('end factorial')
    return total

while True:
    i = 1;
    print(factorial(i))
    i += 1

logging.debug('end log')