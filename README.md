# python-tutorial-by-Vamei

- Python基础（上）
> 添加注释：#!/usr/bin/env python 变成可执行脚本
修改文件权限：chmod 755 hello.py （r:4 w:2 x:1）
执行脚本：./hello.py （仅linux系统）

- Python基础（下）
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
    文本读取
    >>>f = open('test.txt','r')
    >>>content = f.read(N)
    >>>content = f.readline()
    >>>content = f.readlines()
    文本写入
    >>>f.write('I like apple!\n')
    关闭文件
    >>>f.close()
> 模块：
    模块引入方式：
    import a as b             # 引入模块a，并将模块a重命名为b
    from a import function1   # 从模块a中引入function1对象。
    from a import *           # 从模块a中引入所有对象。
    功能相似的模块放在同一个文件夹this_dir里：import this_dir.module
    搜索路径：
    程序所在的文件夹
    操作系统环境变量PYTHONPATH所包含的路径
    标准库的安装路径
> 函数参数传递：传递方式可混合，顺序原则为：先位置，再关键字，再包裹位置，再包裹关键字。

- Python进阶（下）
> 循环设计：range、enumerate、zip
> 循环对象: 它包含有一个next()方法的对象