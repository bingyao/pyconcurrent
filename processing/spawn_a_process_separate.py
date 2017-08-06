import multiprocessing
import spawn_a_process_target as spawn_target

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=spawn_target.foo, args=(i,))
        p.start()
        p.join()

