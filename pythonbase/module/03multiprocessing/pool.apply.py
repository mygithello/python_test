import multiprocessing
import os
import time

def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name, os.getpid(), os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))

if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')


"""
pool.apply
apply(func[, args[, kwds]])
该方法只能允许一个进程进入池子，在一个进程结束之后，另外一个进程才可以进入池子。
"""
