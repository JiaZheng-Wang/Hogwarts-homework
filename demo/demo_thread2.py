# @Time    : 2020/12/2 18:00
# @Author  : Sylar
# @Explain : 
# @Software: PyCharm


import logging
import threading
import _thread
from time import sleep, ctime, time
logging.basicConfig(level=logging.INFO)
loops = [2, 4]


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    logging.info("start loop " + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + "at" + ctime())


def main():

    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        # threads[i].setDaemon(True)
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
# for i in range(4):
#     t.join()
