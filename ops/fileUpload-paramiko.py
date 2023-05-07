
# 上传文件至指定服务器
# paramiko 遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接，可以实 现远程文件的上传，下载或通过ssh远程执行命令。
# 使用pip命令进行安装：pip install paramiko

# cat paramikosend.py
import paramiko
import datetime
import os  # 导入包
hostname = 'ip'  # 上传文件到该服务器
username = 'root'
password = '123456'
port = 22
local_dir = '/root/paramiko'  # 本地路径
remote_dir = '/root/paramiko'  # 远程路径
try:
    #  这段逻辑不用改
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = os.listdir(local_dir)  # 获取文件目录内容
    for f in files:
        sftp.put(os.path.join(local_dir, f), os.path.join(remote_dir, f))
        # 上传文件,下载使用sftp.get
    t.close()
except Exception as e:
    print("connect error!:", e)
