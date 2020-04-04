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
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')

"""

Pool 可以提供指定数量的进程供用户使用，默认是 CPU 核数。当有新的请求提交到 Poll 的时候，如果池子没有满，会创建一个进程来执行，------------否则就会让该请求等待。
- Pool 对象调用 join 方法会等待所有的子进程执行完毕
- 调用 join 方法之前，必须调用 close
- 调用 close 之后就不能继续添加新的 Process 了

pool.apply_async
apply_async 方法用来同步执行进程，允许多个进程同时进入池子。
"""