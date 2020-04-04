from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行的代码:
def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())
# 读数据进程执行的代码:
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)
if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q =  ()
    proc_writer1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target=proc_write, args=(q,['url_4','url_5','url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程proc_writer，写入:
    proc_writer1.start()
    proc_writer2.start()
    # 启动子进程proc_reader，读取:
    proc_reader.start()
    # 等待proc_writer结束:
    proc_writer1.join()
    proc_writer2.join()
    # proc_reader进程里是死循环，无法等待其结束，只能强行终止:
    proc_reader.terminate()


"""
Queue 进程间通信
Queue 用来在多个进程间通信。Queue 有两个方法，get 和 put。

put 方法
Put 方法用来插入数据到队列中，有两个可选参数，blocked 和 timeout。
- blocked = True（默认值），timeout 为正

该方法会阻塞 timeout 指定的时间，直到该队列有剩余空间。如果超时，抛出 Queue.Full 异常。


blocked = False
如果 Queue 已满，立刻抛出 Queue.Full 异常
get 方法
get 方法用来从队列中读取并删除一个元素。有两个参数可选，blocked 和 timeout
- blocked = False （默认），timeout 正值

等待时间内，没有取到任何元素，会抛出 Queue.Empty 异常。


blocked = True
Queue 有一个值可用，立刻返回改值；Queue 没有任何元素，
"""