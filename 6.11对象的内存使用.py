# coding=utf-8


# 内置函数id能够显示变量的内存地址
a = 1
print(id(a))
print(hex(id(a)))

# 创建多个等于1的引用时，引用指向的是同一个对象
a = 1
b = 1
print(id(a))
print(id(b))


# 判断是否为同一个对象
# True
a = 1
b = 1
print(a is b)

# True
a = "good"
b = "good"
print(a is b)

# False
a = "very good morning"
b = "very good morning"
print(id(a))
print(id(b))
print(a is b)

# False
a = []
b = []
print(a is b)

# 利用getrefcount记录引用的次数，本身自带一次引用
from sys import getrefcount

print(getrefcount([1,2,3]))

a = [1, 2, 3]
print(getrefcount(a))

b = a
print(getrefcount(b))