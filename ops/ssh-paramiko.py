
# paramiko执行其它服务器命令

# 完全不需要修改

# paramiko 遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接，可以实 现远程文件的上传，下载或通过ssh远程执行命令。
# 使用pip命令进行安装：pip install paramiko

#!/usr/bin/python

import paramiko

ip = input("请输入需要远程的主机IP地址:")
uname = input("请输入登录用户名:")
pword = input("请输入登录密码:")

# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname=ip, port=22, username=uname, password=pword)

# 手动输入待执行命令
mycmd = input("请输入需要执行的命令:")
stdin, stdout, stderr = ssh.exec_command(mycmd)
# 用于测试:直接执行指定命令
# ssh.exec_command('cd /tmp/ && touch paramiko.txt && echo "hello 少年" > paramiko.txt')

# 结果放到stdout中，如果有错误将放到stderr中
print("返回结果:", stdout.read().decode())
print("错误信息:", stderr.read().decode())

# 关闭连接
ssh.close()
