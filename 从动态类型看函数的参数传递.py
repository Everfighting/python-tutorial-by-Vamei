# coding=utf-8
def f(x):
    x = 100
    print x

a = 1
f(a)
print a
#改变了引用。

def f(x):
    x[0] = 100
    print x

a = [1,2,3]
f(a)
print a
#改变了引用对象。