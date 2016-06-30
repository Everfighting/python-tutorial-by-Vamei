# coding=utf-8
class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age
    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0: return True
            else: return False
        else: raise AttributeError(name)

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)

print(summer.male)

#还设有 __setattr__(self, name, value)和__delattr__(self, name)可用于修改和删除属性.
# 暂未完全理解。
