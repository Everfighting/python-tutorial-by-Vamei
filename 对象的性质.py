# coding=utf-8
#!/usr/bin/env python
class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    # def printGender(self):
    #     print self.gender

li_lei = Human('male') # 'male'递给__init__()方法
print li_lei.gender   #这一行结果与下一行对比
# li_lei.printGender()   #这一行结果与上一行对比

# 若没有定义printGender方法，则li_lei.printGender发生错误
