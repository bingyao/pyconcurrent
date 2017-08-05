from threading import Thread

from time import sleep

class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel Python!"


    def print_message(self):
        print(self.message)


    def run(self):
        print('Thread Starting...\n')

        x = 0
        while(x<10):
            self.print_message()
            sleep(2)
            x += 1

        print('Thread Ended.\n')


print('Process Started.')

hello_parallel = CookBook()

hello_parallel.start()

print('Process Ended.')
