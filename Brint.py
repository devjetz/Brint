from datetime import datetime, date
import time
import sys
from os import system
# \033[1;94mINFO
# \033[0;35m
inputt = {
    't': '\033[1;94m~>     \033[0m'
}


def timer(func):
    timestamp = datetime.now().strftime(f"%H:%M:%S")
    today = date.today()
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(print('\033[1;30m{} {} \033[1;94mTIMER    \033[0m\033[0;34m{} \033[0mFunction ran in {} second(s).'.format(today, timestamp, func.__name__, t2)))
    return wrapper
    

def info(highlight, *arg, **kwarg):
    timestamp = datetime.now().strftime(f"%H:%M:%S")
    today = date.today()
    print('\033[1;30m{} {} \033[1;94mINFO     \033[0m\033[0;34m{} \033[0m{}'.format(today, timestamp, highlight, ' '.join(map(str, arg))), **kwarg)

def error(highlight, *arg, **kwarg):
    timestamp = datetime.now().strftime(f"%H:%M:%S")
    today = date.today()
    print('\033[1;30m{} {} \033[1;91mERROR    \033[0m\033[0;34m{} \033[0m{}'.format(today, timestamp, highlight, ' '.join(map(str, arg))), **kwarg)

def success(highlight, *arg, **kwarg):
    timestamp = datetime.now().strftime(f"%H:%M:%S")
    today = date.today()
    print('\033[1;30m{} {} \033[1;32mOK       \033[0m\033[0;34m{} \033[0m{}'.format(today, timestamp, highlight, ' '.join(map(str, arg))), **kwarg)

def input(highlight, *arg, **kwarg):
    inputt = '\033[1;94m~>     \033[0m'
    timestamp = datetime.now().strftime(f"%H:%M:%S")
    today = date.today()
    print('\033[1;30m{} {} \033[1; mINPUT    \033[0m\033[0;34m{} \033[0m{}'.format(today, timestamp, highlight, ' '.join(map(str, arg))), **kwarg)


@timer
def test():
    info('TEST','Test went successfull on print.')
    error('TEST','Test went successfull on print.')
    success('TEST','Test went successfull on print.')
    input('TEST','Test went successfull on print.')
