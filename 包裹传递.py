# coding=utf-8
#!/usr/bin/env python
#包裹传递用于用户不知道参数个数的情况
def func(*name):
    print type(name)
    print name

# 按照位置传入tuple
func(1,4,6)
func(5,6,7,1,2,3)

def func1(**dict):
    print type(dict)
    print dict

#按照关键词传入dic
func1(a=1,b=9)
func1(m=2,n=1,c=11)

#difference between * and **

def func2(a,b,c):
    print a,b,c

args = (1,3,4)
func2(*args)

dict = {'a':1,'b':2,'c':3}
func2(**dict)