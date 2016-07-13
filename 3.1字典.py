# coding=utf-8
dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print dic[key]

del dic['tom']  # 删除 dic 的‘tom’元素
print dic.keys()  # 返回dic所有的键
print dic.values()  # 返回dic所有的值
print dic.items()  # 返回dic所有的元素（键值对）


dic.clear()  # 清空dic，dict变为{}

print len(dic)  # 字典中元素个数