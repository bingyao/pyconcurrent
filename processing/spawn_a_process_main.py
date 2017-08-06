import multiprocessing

def foo(i):
    print('This function is called in process {}.'.format(i))

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()
        p.join()
