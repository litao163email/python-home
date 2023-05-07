#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
import smtplib
from email.mime.text import MIMEText

# 设置阈值
THRESHOLD = 0

# 邮件相关配置
SMTP_SERVER = 'smtp.163.com'
SMTP_PORT = 25
EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成你的电子邮件地址
EMAIL_PASSWORD = 'ZKLWMFMPSCKOWQVQ'  # 替换成你的电子邮件密码(注意是授权码不是登录密码)
TO_EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成接收者的电子邮件地址

# 获取CPU使用率
cpu_percent = psutil.cpu_percent()

# 如果CPU使用率超过阈值，则发送电子邮件
if cpu_percent > THRESHOLD:
    # 获取CPU占用高的进程
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'exe', 'connections']):
        try:
            cpu_usage = process.cpu_percent()
            if cpu_usage > THRESHOLD:
                # 获取该进程的端口信息
                connections = process.connections()
                ports = [
                    conn.laddr.port for conn in connections if conn.status == psutil.CONN_LISTEN]
                if ports:
                    port_str = ','.join(str(port) for port in ports)
                else:
                    port_str = 'N/A'

                # 将进程的信息添加到列表中
                processes.append({'pid': process.pid, 'name': process.name(
                ), 'exe': process.exe(), 'port': port_str})
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # 如果有CPU占用高的进程，则发送电子邮件
    if processes:
        # 构造邮件内容
        message = '以下进程占用了CPU过高：\n\n'
        for process in processes:
            message += f"进程ID: {process['pid']}\n进程名称: {process['name']}\n可执行文件: {process['exe']}\n端口: {process['port']}\n\n"
        message += f"CPU使用率为 {cpu_percent}%"

        # 将邮件内容转换为MIME格式
        message = MIMEText(message)

        # 设置邮件主题、发件人、收件人
        message['subject'] = f"CPU使用率超过阈值 ({cpu_percent}%)"
        message['From'] = EMAIL_ADDRESS
        message['To'] = TO_EMAIL_ADDRESS

        # 连接SMTP服务器并登录
        smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # 发送邮件
        smtp_server.sendmail(
            EMAIL_ADDRESS, TO_EMAIL_ADDRESS, message.as_string())

        # 关闭连接
        smtp_server.quit()
