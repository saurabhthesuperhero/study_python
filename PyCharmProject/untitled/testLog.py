import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start log')

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

print(factorial(5))
logging.debug('end log')