import threading
import time


def print_age(who, age):
    print("Hello,every one!")
    time.sleep(1)
    print("%s is %s years old !" % (who, age))


def daemon_func():
    for i in range(18, 25):
        t = threading.Thread(target=print_age, args=("Jet", i,))  # 创建线程
        t.start()

"""
可以通过setDaemon()方法将线程设置为守护线程,当守护线程退出时,由它启动的其它子线程将同时退出,不管是否执行完成
"""
if __name__ == "__main__":
    dt = threading.Thread(target=daemon_func)     # 创建线程
    dt.setDaemon(True)      # 设置为守护线程
    dt.start()
    dt.join(timeout=2)
    print("over...")
