import redis

# 选择连接的数据库
db = input('输入数据库:')
r = redis.Redis(host=db, port=6379, db=0)

# 输入要匹配的键名
id = input('请输入要执匹配的字段：')
arg = '*' + id + '*'

n = r.keys(arg)
# 查看匹配到键值
for i in n:
    print(i.decode('utf-8'))

# 确定清除的键名
delid = input('输入要删除的键：')

print('清除缓存 %s 成功' % delid)
