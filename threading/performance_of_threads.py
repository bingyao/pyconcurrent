from timeit import Timer
from threading import Thread

def function_to_run():
    pass


class ParObj(Thread):

    def run():
        function_to_run()


class SeqObj():

    def run():
        function_to_run()


def run_sequence(n):
    seqs = []
    for _ in range(n):
        seqs.append(SeqObj())

    for i in range(n):
        seqs[i].run()


def run_parrallel(n):
    threads = []
    for _ in range(n):
        threads.append(ParObj())

    for i in range(n):
        threads[i].run()
    for i in range(n):
        threads[i].join()


def show_results(fun_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))

if __name__ == '__main__':
    repead = 100
