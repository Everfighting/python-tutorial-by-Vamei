# coding=utf-8
re = map((lambda x: x+3),[1,3,5,6])
print re
# map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。

def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func,[10,56,101,500])
# 如果函数对象返回的是True，则该次的元素被储存于返回的表中。 filter通过读入的函数来筛选数据。

print reduce((lambda x,y: x+y),[1,2,5,7,9])
# reduce可以累进地将函数作用于各个参数。