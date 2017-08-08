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
    cp = multiprocessing.current_process()
    name = cp.name
    pid = cp.pid
    time.sleep(3)
    print('The foo is called by [{}] named {} in loop {}'.format(pid, name, i))

if __name__ == '__main__':
    info('MAIN LINE.')
    plist = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        plist.append(p)
        p.start()
        p.join()

    # print()

    # for i in range(5):
    #     plist[i].join()
