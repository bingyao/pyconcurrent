import multiprocessing
import time

def foo(i):
    name = multiprocessing.current_process().name
    print('This function is called by No{} process named {}'.format(i, name))


if __name__ == '__main__':
    p_named = multiprocessing.Process(name='Hello', target=foo, args=(0,))
    p_unnamed = multiprocessing.Process(target=foo, args=(1,))
    p_named.start() 
    p_unnamed.start() 

