import multiprocessing as mp
import time
import random


class Producer(mp.Process):
    
    def __init__(self, queue):
        mp.Process.__init__(self)
        self.queue = queue
        # self.name = mp.current_process().name
        # self.pid = mp.current_process().pid


    def produce(self):
        cargo = random.randint(0, 256)
        self.queue.put(cargo)
        print('PRODUCER: cargo {} is append by {}:{}'.format(cargo, self.pid, self.name))
        time.sleep(1)
        # print('PRODUCER: queue size: {}'.format(self.queue.qsize()))
        # Note that this may raise NotImplementedError on Unix platforms 
        # like Mac OS X where sem_getvalue() is not implemented.


    def run(self):
        for i in range(10): self.produce()



class Comsumer(mp.Process):
    
    def __init__(self, queue):
        mp.Process.__init__(self)
        self.queue = queue
        # self.name = mp.current_process().name
        # self.pid = mp.current_process().pid


    def comsume(self):
        time.sleep(1)
        cargo = self.queue.get()
        print('COMSUMER: cargo {} is fetched by {}:{}'.format(cargo, self.pid, self.name))


    def run(self):
        while True:
            time.sleep(1)
            if self.queue.empty():
                print('COMSUMER: Queue is empty.')
                break
            else:
                self.comsume()


if __name__ == '__main__':
    queue = mp.Queue()
    p = Producer(queue)
    c = Comsumer(queue)
    p.start()
    c.start()
    p.join()
    c.join()
