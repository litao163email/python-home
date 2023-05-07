
# 传可变对象实例

def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

print("------------------------------")

# 默认参数


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")

print("------------------------------")

# 不定长参数


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

print("------------------------------")

# 匿名函数lambda
# python 使用 lambda 来创建匿名函数


def sum(arg1, arg2): return arg1 + arg2


# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))
