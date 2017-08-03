import threading

shared_with_lock = 0
shared_without_lock = 0
COUNT = 1000000
resource_lock = threading.Lock()

def increment_with_lock():
    global shared_with_lock
    for i in range(COUNT):
        resource_lock.acquire()
        shared_with_lock += 1
        resource_lock.release()

def decrement_with_lock():
    global shared_with_lock
    for i in range(COUNT):
        resource_lock.acquire()
        shared_with_lock -= 1
        resource_lock.release()

def increment_without_lock():
    global shared_without_lock
    for i in range(COUNT):
        shared_without_lock += 1

def decrement_without_lock():
    global shared_without_lock
    for i in range(COUNT):
        shared_without_lock -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    # Without Join, the print funcs will execute first before t1 and t2
    # finished, so is SEEMS LIKE even with lock will fail.
    
    print('Value with Lock: {}'.format(shared_with_lock))
    print('Value without Lock: {}'.format(shared_without_lock))
    print('t1 still alive? {}'.format(t1.is_alive()))
    print('t2 still alive? {}'.format(t2.is_alive()))
    print('t3 still alive? {}'.format(t3.is_alive()))
    print('t4 still alive? {}'.format(t4.is_alive()))
