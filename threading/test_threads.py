import threading
import time

def example(i):
    print('example function is called by thread {}'.format(i))

def first_fun():
    print(threading.current_thread().name + ' is Starting {}.'.format(threading.current_thread().ident))
    time.sleep(2)
    print(threading.current_thread().name + ' is Exiting.')
    
def second_fun():
    print(threading.current_thread().name + ' is Starting {}.'.format(threading.current_thread().ident))
    time.sleep(2)
    print(threading.current_thread().name + ' is Exiting.')

def third_fun():
    print(threading.current_thread().name + ' is Starting {}.'.format(threading.current_thread().ident))
    time.sleep(2)
    print(threading.current_thread().name + ' is Exiting.')

# threads = []
# for i in range(5):
#     t = threading.Thread(target=example, args=(i, ))
#     threads.append(t)
#     t.start()
#     t.join()

if __name__ == '__main__':

    t1 = threading.Thread(target=first_fun)
    t2 = threading.Thread( target=second_fun)
    t3 = threading.Thread(target=third_fun)

    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
