# python-tutorial-by-Vamei

- Python基础上
> 添加注释：#!/usr/bin/env python 变成可执行脚本
修改文件权限：chmod 755 hello.py （r:4 w:2 x:1）
执行脚本：./hello.py （仅linux系统）

- Python基础下
> 循环：

    for 元素 in 序列:
        statement

    while 条件:
        statement

    for i in range(10):
        if i == 2:
            continue
        print i

> 函数：
1、值传递与指针传递
2、类、属性
3、方法
4、继承

> 面向对象的进一步拓展：
1、调用其他信息
2、__init()__
3、对象的性质
4、内置函数：dir() 查询属性和 help()查询说明文档

- Python进阶(上)
> 字典：
    >>>print dic.keys()           # 返回dic所有的键
    >>>print dic.values()         # 返回dic所有的值
    >>>print dic.items()          # 返回dic所有的元素（键值对）
    >>>dic.clear()                # 清空dic，dict变为{}
    >>>del dic['tom']             # 删除 dic 的‘tom’元素
    >>>print len(dic)             # 字典中元素个数
> 文本文件的输入输出:


