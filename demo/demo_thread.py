# # @Time    : 2020/12/2 14:35
# # @Author  : Sylar
# # @Explain :
# # @Software: PyCharm
# import logging
# import threading
# import _thread
# from time import sleep, ctime, time
#
# logging.basicConfig(level=logging.INFO)
#
#
# # def loop0():
# #     logging.info("start loop0 at" + ctime())
# #     sleep(2)
# #     logging.info("end loop0 at" + ctime())
# #
# #
# # def loop1():
# #     logging.info("start loop1 at" + ctime())
# #     sleep(2)
# #     logging.info("end loop1 at" + ctime())
#
# #
# # def main():
# #     logging.info("start all at" + ctime())
# #     _thread.start_new_thread(loop0, ())
# #     _thread.start_new_thread(loop1, ())
# #     sleep(4)  # _thread没有守护线程的概念，进程退出，线程就结束
# #     logging.info("end all" + ctime())
# #
#
#
# #
# # if __name__ == '__main__':
# #     main()
#
# class MyThread(threading.Thread):
#
#     def __init__(self, func):
#         super(MyThread, self).__init__()
#         self.func = func
#
#     def run(self):
#         self.func()
#
#
# def loop():
#     logging.info("start loop at" + ctime())
#     sleep(6)
#     logging.info("end loop at" + ctime())
#
#
# def main():
#     logging.info("start all at" + ctime())
#     threads=[]
#     for i in range(4):
#         t = MyThread(loop)
#         threads.append(t)
#     for i in range(4):
#         threads[i].start()
#     logging.info("end all at" + ctime())
#
# if __name__ == '__main__':
#     main()
# # for i in range(4):
# #     t.join()
#
# # 原语
# ## 锁
# ## 信号量


import threading
import time

def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':

    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
    for t in thread_list:
        t.join()
    print('主线程结束！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)