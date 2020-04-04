

import multiprocessing
import os

def run_proc(name):
    print('Child process {0} {1} Running '.format(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()
    p.join()
    print('Process close')





"""
Process 类
Process 类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成 Process 示例的创建。

star() 方法启动进程，
join() 方法实现进程间的同步，等待所有进程退出。
close() 用来阻止多余的进程涌入进程池 Pool 造成进程阻塞。
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
1
target 是函数名字，需要调用的函数
args 函数需要的参数，以 tuple 的形式传入
————————————————
版权声明：本文为CSDN博主「Citizen_Wang」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/CityzenOldwang/article/details/78584175
"""


