import logging
import threading
from queue import Queue
from threading import Thread, Condition

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 1024, 7]

queue_condition = Condition()

def fibonacci_task(condition):

    name = threading.current_thread().name
    with condition:
        while shared_queue.empty():
            logger.info("[{}] - waiting for elements in queue..".format(name))
            condition.wait()
        else:
            value = shared_queue.get()
            a, b = 0, 1
            for item in range(value):
                a, b = b, a + b
                fibo_dict[value] = a
            shared_queue.task_done()
            logger.debug("[{}] fibonacci of key [{}] with result [{}]".format(
                           name, value, fibo_dict[value]))


def queue_task(condition):
    logging.debug('Starting queue_task...')
    with condition:
        for item in input_list:
            shared_queue.put(item)
        logging.debug("Notifying fibonacci_task threads that the queue is ready to consume..")
        condition.notify_all()


threads = [Thread(target=fibonacci_task, args=(queue_condition,), daemon=True) for i in range(4)]

[thread.start() for thread in threads]

prod = Thread(name='queue_task_thread', daemon=True, target=queue_task, args=(queue_condition,))
prod.start()

[thread.join() for thread in threads]

print(fibo_dict)
