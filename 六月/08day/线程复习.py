# 线程是为了实现多任务
#
# 线程是依赖与进程存在的，并且一个进程下，可以有多个线程
# 线程共享资源，在Python中多线程并发进行的，GIL（全局解释器锁），所以同一时刻只有一个线程被执行。鲜橙多用于I/O密集型操作（文件写读操作，I/O）

# 线程自执行式无序的
#线程之间的资源是共享的
#线程锁的作用：

import threading

