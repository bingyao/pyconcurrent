from threading import Thread, Event
import time
import random

items = []
event = Event()

class Consumer(Thread):

    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def consume(self):
        self.event.wait()
        item = self.items.pop()
        print('Consumer: {} is consumed by {}!\n'.format(self.name, item))

    def run(self):
        while True:
            time.sleep(1)
            self.consume()


class Producer(Thread):
    
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def produce(self):
        item = random.randint(0,256)
        self.items.append(item)
        print('Produer: {} produced item {}'.format(self.name, item))
        self.event.set()
        self.event.clear()

    def run(self):
        # global items
        for i in range(10):
            print('Round {}.'.format(i))
            time.sleep(2)
            self.produce()


if __name__ == '__main__':
    t1 = Producer(items, event)
    t2 = Consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(items)
