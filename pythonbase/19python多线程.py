import threading
import time


def print_age(who, age):
    """
    需要用多线程调用的函数
    :param who:
    :param age:
    :return:
    """
    print("Hello,every one!")
    time.sleep(1)
    print("%s is %s years old !" % (who, age))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_age, args=("jet", 18, ))     # 创建线程1
    t2 = threading.Thread(target=print_age, args=("jack", 25, ))    # 创建线程2
    t3 = threading.Thread(target=print_age, args=("jack2", 25,))     # 创建线程3
    t1.start()    # 运行线程1
    t2.start()    # 运行线程2
    t3.start()    # 运行线程3
    print("over...")