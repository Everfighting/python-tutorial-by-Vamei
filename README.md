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
> 循环对象: 包含有一个next()方法的对象
  迭代器: 要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。
  生成器：生成器的编写方法和函数定义类似，只是在return的地方改为yield。
  表推导：表推导(list comprehension)是快速生成表的方法。
> 函数对象：lambda函数、函数作为参数传递、
    map()函数、filter()函数、reduce()函数
> 错误处理：
异常处理：
抛出异常：如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。
> 动态类型：
列表可以通过引用其元素，改变对象自身(in-place change)。这种对象类型，称为可变数据对象(mutable object)，词典也是这样的数据类型。
而像之前的数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象(immutable object)。
我们之前学的元组(tuple)，尽管可以调用引用元素，但不可以赋值，因此不能改变对象自身，所以也算是immutable object。
> 从动态类型看函数的参数传递：函数的参数传递，本质上传递的是引用。
如果传递的是可变(mutable)的对象，那么改变函数参数，有可能改变原对象。所有指向原对象的引用都会受影响。
- Python深入（上）
> 运算符: Python的运算符是通过调用对象的特殊方法实现的.
内置函数：len()
表元素引用：list.__getitem__(3)
对象的属性：

- Python深入（下）
>

- Python补充
>序列的方法


>Python小技巧
import模块


查询





使用中文(以及其它非ASCII编码)





表示2进制，8进制和16进制数字


注释


搜索路径


脚本与命令行结合



安装非标准包




Python内置函数清单
1、数学运算
2、类型转换
3、序列操作
4、类、对象、属性
5、编译、执行
6、其他


字符串格式化（%操作符)
模板
格式符



