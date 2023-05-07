
# 获取cpu、磁盘等信息

# sutil是一个跨平台库，能够轻松实现获取系统运行的进程和系统利用率（包括CPU、 内存、磁盘、网络等）信息,它主要应用于系统监控。

import psutil

# 查看cpu所有信息
print("---------------cpu所有信息--------------------")
print(psutil.cpu_times())

# 获取磁盘完整信息
print("---------------磁盘完整信息--------------------")
print(psutil.disk_partitions())

print()

print("---------------系统所有进程ID--------------------")
print(psutil.pids())

print("---------------查看单个进程详细情况--------------------")
p = psutil.Process(372)
print(p)  # 进程ID

print("---------------其进程的某个状态--------------------")

print(p.name())
# p.name()          #进程名
# p.exe()             #进程的bin路径
# p.cwd()            #进程的工作目录绝对路径
# p.status()         #进程状态
# p.create_time()      #进程创建时间
# p.uids()           #进程uid信息
# p.gids()           #进程的gid信息
# p.cpu_times()     #进程的cpu时间信息,包括user,system两个cpu信息
# p.cpu_affinity()   #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就 好
# p.memory_percent()    #进程内存利用率
# p.memory_info()          #进程内存rss,vms信息
# p.io_counters()            #进程的IO信息,包括读写IO数字及参数
# p.connectios()            #返回进程列表
# p.num_threads()         #进程开启的线程数
