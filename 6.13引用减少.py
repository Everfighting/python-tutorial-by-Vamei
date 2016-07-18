# coding=utf-8
from sys import getrefcount

a = [1, 2, 3]
b = a
print(getrefcount(b))
# 使用del关键字删除某个引用
del a
print(getrefcount(b))
print b

# del也可以用于删除容器元素中的元素
a = [1,2,3]
del a[0]
print(a)

# 如果某个引用指向对象A，当这个引用被重新定向到某个其他对象B时，对象A的引用计数减少
from sys import getrefcount

a = [1, 2, 3]
b = a
print(getrefcount(b))

a = 1
print(getrefcount(b))