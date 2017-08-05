from threading import Thread, Condition
import time

items = []
condition = Condition()


class Consumer(Thread):
    
    def __init__(self):
        Thread.__init__(self)


    def consume(self):
        global items
        global condition

        condition.acquire()
        if not items:
            print('Consumer INFO: waiting...')
            condition.wait()
        items.pop()
        print('Consumer INFO: consumed 1 item, {} items left.'.format(len(items)))
        condition.notify()
        condition.release()
        
    def run(self):
        for _ in range(20):
            time.sleep(2)
            self.consume()


class Producer(Thread):
    
    def __init__(self):
        Thread.__init__(self)


    def produce(self):
        global items
        global condition

        condition.acquire()
        if len(items) == 10:
            print('Producer INFO: Halt for producing...')
            condition.wait()
        items.append(1)
        print('Producer INFO: Total {} items are produced.'.format(len(items)))
        condition.notify()
        condition.release()


    def run(self):
        for _ in range(30):
            time.sleep(1)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
