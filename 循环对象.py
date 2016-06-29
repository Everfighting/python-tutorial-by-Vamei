# coding=utf-8
for line in open('test.txt'):
    print line

    # for结构自动调用next()方法，将该方法的返回值赋予给line。
    # 循环知道出现StopIteration的时候结束。