# coding=utf-8
nl = [1,2,5,3,5]
print nl.count(5)       # 计数，看总共有多少个5
print nl.index(3)       # 查询 nl 的第一个3的下标

nl.append(6)            # 在 nl 的最后增添一个新元素6
print nl

nl.sort()               # 对nl的元素排序
print nl

nl.pop()          # 从nl中去除最后一个元素，并将该元素返回。
print nl

nl.remove(2)            # 从nl中去除第一个2
print nl

nl.insert(0,9)          # 在下标为0的位置插入9
print nl

# 有的可以直接运用方法print出来，有的则需要先运用方法，后才能够print整个list
# 区别在哪里?
# 直接print list.attribute 中并没有改变list的元素
# 改变了list的元素则不能够直接print
