
# -*- coding: utf-8 -*-
import threading
import time


def add_one():
    global num
    semaphore.acquire()    # 加锁,最多有五个线程做以下操作
    time.sleep(1)
    num -= 1
    print("Value: %s" % num)
    semaphore.release()    # 释放锁

"""
信号量semaphore,是一个变量，控制着对公共资源或者临界区的访问。信号量维护着一个计数器，指定可同时访问资源或者进入临界区的线程数。用来控制最大线程数的
"""

if __name__ == "__main__":
    num = 100
    thread_list = []
    semaphore = threading.BoundedSemaphore(5)

    for i in range(100):
        t = threading.Thread(target=add_one)
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()        # 等待线程结束
    print("Num = %s" % num)