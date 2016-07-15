# coding=utf-8
def func(x, y):
    return x + y

def test(f, a, b):
    print 'test'
    print f(a, b)

test(func, 3, 5)

