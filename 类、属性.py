# coding=utf-8
# usr/bin/env python

# 属性相近把东西归类
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

summer = Bird()
print summer.way_of_reproduction
print summer.have_feather
# 对属性的引用是通过 对象.属性（object.attribute） 的形式实现的。
