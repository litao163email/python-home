#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用 psutil 库监控 CPU 使用率并发送警报


import psutil
import smtplib
from email.mime.text import MIMEText

# 设置阈值
THRESHOLD = 1

# 邮件相关配置
SMTP_SERVER = 'smtp.163.com'
SMTP_PORT = 25
EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成你的电子邮件地址
EMAIL_PASSWORD = 'ZKLWMFMPSCKOWQVQ'  # 替换成你的电子邮件密码(注意是授权码不是登录密码)
TO_EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成接收者的电子邮件地址

# 获取CPU使用率
cpu_usage = psutil.cpu_percent()

# 如果CPU使用率超过阈值，则发送电子邮件
if cpu_usage > THRESHOLD:
    # 构造邮件内容
    message = MIMEText(f"CPU usage is {cpu_usage}%")
    message['subject'] = f"CPU警告:{cpu_usage}%"
    message['From'] = EMAIL_ADDRESS
    message['To'] = TO_EMAIL_ADDRESS

    # 连接SMTP服务器并登录
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # 发送邮件
    smtp_server.sendmail(EMAIL_ADDRESS, TO_EMAIL_ADDRESS, message.as_string())

    # 关闭连接
    smtp_server.quit()
