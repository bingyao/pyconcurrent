import threading
import time
import random

semaphore = threading.Semaphore(0)
# value set to 1 (defaults) will cause the first call of consumer fail.

def consumer():
    print('Consumer is waiting...')
    semaphore.acquire()
    print('Consuming {} items\n'.format(item))

def producer():
    global item
    time.sleep(5)
    item = random.randint(0,10000)
    print('Producing {} items'.format(item))
    semaphore.release()

if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        print(t1.name + ' started.')
        t2.start()
        print(t2.name + ' started.')
        t1.join()
        t2.join()

    print('Finished!')
