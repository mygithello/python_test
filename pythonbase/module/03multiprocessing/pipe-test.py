from multiprocessing import Process, Pipe

def send(pipe):
    pipe.send(['spam'] + [42, 'egg'])   # send 传输一个列表
    pipe.close()

if __name__ == '__main__':
    (con1, con2) = Pipe()                            # 创建两个 Pipe 实例
    sender = Process(target=send, args=(con1, ))     # 函数的参数，args 一定是实例化之后的 Pip 变量，不能直接写 args=(Pip(),)
    sender.start()                                   # Process 类启动进程
    print("con2 got: %s" % con2.recv())              # 管道的另一端 con2 从send收到消息
    con2.close()                                     # 关闭管道

"""
Pipe 进程间通信
常用来在两个进程间通信，两个进程分别位于管道的两端。
multiprocessing.Pipe([duplex])
示例一和示例二，也是网上找的别人的例子，尝试理解并增加了注释而已。网上的例子，大多是例子一和例子二在一起的，这里分开来看，比较容易理解。
"""

