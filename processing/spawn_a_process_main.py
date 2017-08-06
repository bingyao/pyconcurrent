import multiprocessing
import os
import time

def info(title):
    print(title)
    print('The module name is: ', __name__)
    print("The PARENTS' ID is: ", os.getppid())
    print("The process' ID is: ", os.getpid())


def foo(i):
    info('\nfunction FOO.')
    name = multiprocessing.current_process().name
    time.sleep(5)
    print('The foo is called by process {} in loop {}'.format(name, i))

if __name__ == '__main__':
    info('MAIN LINE.')
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
        p.join()
