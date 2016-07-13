# coding=utf-8
def gen():
    for i in range(4):
        yield i

G = (x for x in range(4))
print G

# 这部分需要补充关于迭代器与生成器的知识，教程中说的不是很详细。