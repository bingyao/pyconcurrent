import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print('Starting {}'.format(name))
    time.sleep(3)
    print('Exiting {}'.format(name))


if __name__ == '__main__':
    pbg = multiprocessing.Process(target=foo, name='Background Process')
    pbg.daemon = True
    pfg = multiprocessing.Process(target=foo, name='Foreground Process')

    pbg.start()
    pfg.start()
    # pbg.join()
    # pfg.join()
