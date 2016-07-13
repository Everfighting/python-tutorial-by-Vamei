# coding=utf-8
#!/usr/bin/env python
class Bird(object):
    have_feather = True
    way_of_reproduction  = 'egg'

class happyBird(Bird):
    def __init__(self,more_words):
        print 'We are happy birds.',more_words

summer = happyBird('Happy,Happy!')
