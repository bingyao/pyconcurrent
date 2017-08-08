import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    pid = multiprocessing.current_process().pid
    print('Entering process {}:{}'.format(name, pid))
    time.sleep(3)
    print('Exiting process {}:{}'.format(name, pid))


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Before: ', p, p.is_alive())
    p.start()
    print('Start: ', p, p.is_alive())
    p.join()
    p.terminate()
    print('Join: ', p, p.is_alive())
    print('Code: ', p, p.exitcode)
