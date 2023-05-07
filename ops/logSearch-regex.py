#! E:\python3
# -*- coding: UTF-8 -*-

# 使用 regex 库解析日志文件并提取有用信息
# regex 库提供了丰富的正则表达式工具，可以方便地提取有用的信息
# 下载:pip install regex

import regex

# 这和try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 读取日志文件
with open('log.text', 'r') as f:
    log = f.read()

    # 使用正则表达式匹配错误信息（找出所有ERROR:中换行后的所有信息）
    errors = regex.findall(r'ERROR:+/s(.*)', log)

    # 打印出所有匹配到的错误信息
    for error in errors:
        print(error)
