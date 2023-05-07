#!/usr/bin/python
# -*- coding: UTF-8 -*-

# PyMysql的安装很简单：pip install pymysql
import pymysql


try:
    # 打开数据库连接
    db = pymysql.connect(host='10.92.226.28', user='SCPTPMS',
                         passwd='MS@123nfdw', port=3306, db='scptpms_test')
    print('连接成功！')
except:
    print('连接失败!')
    # 就算走了except，还是会继续往下走的，只不过是会打印东西

# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = "SELECT mrsp.settle_month as settleMonth,mrsp.unit_id as unitId  FROM ms_result_smoffi_plant mrsp"

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交修改
#     db.commit()
#     print('数据删除成功')
# except:
#     # 发生错误时回滚
#     db.rollback()

# 获取所有记录列表（py是对空格极其敏感的，注意空格的可能胡导致的错误）
results = cursor.fetchall()
for row in results:
    settleMonth = row[0]
    unitId = row[1]
    # 打印结果
    # print('数据查询成功！')
    print("settleMonth=%s,unitId=%s" %
          (settleMonth, unitId))

# 关闭数据库连接
db.close()
