# coding=utf-8
#!/usr/bin/env python

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    def move(self, dx, dy):
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position

summer = Bird()
print 'after move:',summer.move(5,8)
#方法的第一个参数必须是self，方便自身引用。

class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True

class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False

#Chicken、Oriole继承自Bird

summer = Chicken()
print summer.have_feather
print summer.move(5,8)