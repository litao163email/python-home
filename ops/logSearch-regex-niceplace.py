#! E:\python3
# -*- coding: UTF-8 -*-

# 使用 regex 库解析日志文件并提取有用信息
# regex 库提供了丰富的正则表达式工具，可以方便地提取有用的信息
# 下载:pip install regex

from time import sleep
import regex
import smtplib
from email.mime.text import MIMEText

# 邮件相关配置
SMTP_SERVER = 'smtp.163.com'
SMTP_PORT = 25
EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成你的电子邮件地址
EMAIL_PASSWORD = 'ZKLWMFMPSCKOWQVQ'  # 替换成你的电子邮件密码(注意是授权码不是登录密码)
TO_EMAIL_ADDRESS = 'litao79466@163.com'  # 替换成接收者的电子邮件地址

# 这和try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 读取日志文件
with open('niceplace-backend-0.log', 'r', encoding='UTF-8') as f:

    log = f.read()

    # 使用正则表达式匹配错误信息（找出所有ERROR:中换行后的所有信息）
    # errors = regex.findall(r'ERROR 29606+(.*)', log)
    errors = regex.findall(
        r'^(.*?)ERROR (.*)\n(.*)', log, regex.MULTILINE)

    # 打印出所有匹配到的错误信息
    for error in errors:
        print(error)
        print('\n')

    # 构造邮件内容
    message = MIMEText(f"日志: {errors}%")
    message['subject'] = f"最新日志Error内容"
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
