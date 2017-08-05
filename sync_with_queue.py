import time
import random
from threading import Thread
from queue import Queue

class Consumer(Thread):
    
    def __init__(self, queue):
        Thread.__init__(self)
        self.q = queue

    def consume(self):
        item = self.q.get()
        print('Consumer: {:4d} is consumed by {}'.format(item, self.name))
        self.q.task_done()

    def run(self):
        while True:
            self.consume()


class Producer(Thread):

    def __init__(self, queue):
        Thread.__init__(self)
        self.q = queue

    def produce(self):
        item = random.randint(0, 1024)
        self.q.put(item)
        print('Producer: {} produced {:4d}.'.format(self.name, item))

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    queue = Queue()
    p1 = Producer(queue)
    c1 = Consumer(queue)
    c2 = Consumer(queue)
    c3 = Consumer(queue)
    p1.start()
    c1.start()
    c2.start()
    c3.start()
    p1.join()
    c1.join()
    c2.join()
    c3.join()
