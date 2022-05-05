import logging


logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(message)s')


def add(val_1, val_2):
    return val_1 + val_2

x = 1
y = 2

add_result = add(x,y)
logging.debug('Add: {} + {} = {}'.format(x,y,add_result))
