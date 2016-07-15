# coding=utf-8
def gen():
    for i in range(4):
        yield i

G = (x for x in range(4))
print G

