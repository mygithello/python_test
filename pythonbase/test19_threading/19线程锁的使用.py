# -*- coding: utf-8 -*-
import threading
import time


def add_one():
    global num
    print("Value: %s" % num)
    time.sleep(1)
    lock.acquire()    # 加锁
    num += 1          # 修改数据
    lock.release()    # 释放锁

"""
因为多线程是共享父进程里面的数据的,所以当多个线程同时修改一份数据的时候,就容易出错,因此就有了锁,锁能确保在同一时间只有一个线程修改这份数据
CPython的GIL(Global Interpreter Lock)是全局线程锁,是确保只有一个线程运行的,与这个锁没有关系,锁的层级不一样,GIL更为底层
"""
if __name__ == "__main__":
    num = 0
    lock = threading.RLock()     # 一般都用RLock递归锁
    thread_list = []
    for i in range(1000):
        t = threading.Thread(target=add_one)
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()
    print("Num = %s" % num)