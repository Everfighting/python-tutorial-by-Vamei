# python-tutorial-by-Vamei

- Python基础（上）
    - 添加注释：#!/usr/bin/env python 变成可执行脚本
    - 修改文件权限：chmod 755 hello.py （r:4 w:2 x:1）
    - 执行脚本：./hello.py （仅linux系统）
    - Python序列包括：字符串、列表、元组。元组元素不可变，列表元素可变。
    - 短路逻辑：

            表达式从左至右运算，若 or 的左侧逻辑值为 True ，则短路 or 后所有的表达式（不管是 and 还是 or），直接输出 or 左侧表达式 。
            表达式从左至右运算，若 and 的左侧逻辑值为 False ，则短路其后所有 and 表达式，直到有 or 出现，输出 and 左侧表达式到 or 的左侧，参与接下来的逻辑运算。
            若 or 的左侧为 False ，或者 and 的左侧为 True 则不能使用短路逻辑。

            - 举例如下：
            >>>not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
            >>>4
            分析：
            1.按优先级加括号（not > and > or）
            (not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)

            2.逻辑运算
            规则如下：
            x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
            x or y	布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
            not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
            上式等价于 0 or 0 or 4 or 6 or 9

            3.短路逻辑
            根据短路逻辑：结果为4

- Python基础（下）
    - 循环：

            for 元素 in 序列:
                statement

            while 条件:
                statement

            for i in range(10):
                if i == 2:
                    continue
                print i

            中断条件：
                continue 跳过这一环，进行下一环的操作
                break 停止执行整个循环

    - 函数：

            1、值传递与指针传递的区别
                对于基本数据类型的变量，变量传递给函数之后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（值传递）
                对于表来说，表传递给函数的是一个指针，指针指向的是序列在内存中的位置，在函数中对表的操作将在原有内存中进行，从而影响原有变量。（指针传递）
            2、类、属性
            3、方法：具有“行为”的属性
            4、继承：子类享有父类的所有属性

    - 面向对象的进一步拓展

            1、调用其他信息
            2、__init()__
            3、对象的性质
            4、内置函数：dir() 查询属性和 help()查询说明文档

- Python进阶(上)
    - 字典：

            print dic.keys()           # 返回dic所有的键
            print dic.values()         # 返回dic所有的值
            print dic.items()          # 返回dic所有的元素（键值对）
            dic.clear()                # 清空dic，dic变为{}
            del dic['tom']             # 删除 dic 的‘tom’元素
            print len(dic)             # 字典中元素个数
    - 文本文件的输入输出:

            文本读取
            f = open('test.txt','r')
            content = f.read(N)
            content = f.readline()
            content = f.readlines()

            文本写入
            f.write('I like apple!\n')

            关闭文件
            f.close()

            with可以自动关闭
            with open('/etc/passwd') as

    - 模块：
        - 模块引入方式：

                import a as b             # 引入模块a，并将模块a重命名为b
                from a import function1   # 从模块a中引入function1对象。
                from a import *           # 从模块a中引入所有对象。
                    功能相似的模块放在同一个文件夹this_dir里：import this_dir.module
        - 搜索路径：

                程序所在的文件夹
                操作系统环境变量PYTHONPATH所包含的路径
                标准库的安装路径

        - 模块包：

                功能相似的模块放在同一个文件夹中
                每个文件夹中必须包含__init__.py的文件
                __init__.py可以是空文件



    - 函数参数传递：传递方式可混合，顺序原则为：先位置，再关键字，再包裹位置，再包裹关键字。

- Python进阶（下）
    - 循环设计：range、enumerate、zip
    - 循环对象: 包含有一个next()方法的对象
    - 迭代器: 要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。
    - 生成器：生成器的编写方法和函数定义类似，只是在return的地方改为yield。
    - 表推导：表推导(list comprehension)是快速生成表的方法。
    - 函数对象：lambda函数、函数作为参数传递、map()函数、filter()函数、reduce()函数
    - 错误处理：
    - 异常处理：

            抛出异常：如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。
    - 动态类型：

            列表可以通过引用其元素，改变对象自身(in-place change)。这种对象类型，称为可变数据对象(mutable object)，词典也是这样的数据类型。
            数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象(immutable object)。
            元组(tuple)，尽管可以调用引用元素，但不可以赋值，因此不能改变对象自身，所以也算是immutable object。
    - 从动态类型看函数的参数传递：函数的参数传递，本质上传递的是引用。

            如果传递的是可变(mutable)的对象，那么改变函数参数，有可能改变原对象。所有指向原对象的引用都会受影响。

- Python深入（上）
    - 运算符: Python的运算符是通过调用对象的特殊方法实现的.
    - 内置函数：len()
    - 表元素引用：list.__getitem__(3)
    - 对象的属性：

- Python深入（下）


- Python补充
    - 序列的方法

            len(s)         返回： 序列中包含元素的个数
            min(s)         返回： 序列中最小的元素
            max(s)         返回： 序列中最大的元素
            all(s)         返回： True, 如果所有元素都为True的话
            any(s)         返回： True, 如果任一元素为True的话
            sum(s)         返回：序列中所有元素的和
            s.count(x)     返回： x在s中出现的次数
            s.index(x)     返回： x在s中第一次出现的下标

    - 以下只适合表：

            l.extend(l2)        在表l的末尾添加表l2的所有元素
            l.append(x)         在l的末尾附加x元素
            l.sort()            对l中的元素排序
            l.reverse()         将l中的元素逆序
            l.pop()             返回：表l的最后一个元素，并在表l中删除该元素
            del l[i]            删除该元素

    - 以下用于字符串：

            str为一个字符串，sub为str的一个子字符串。s为一个序列，它的元素都是字符串。width为一个整数，用于说明新生成字符串的宽度。
            str.count(sub)       返回：sub在str中出现的次数
            str.find(sub)        返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
            str.index(sub)       返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
            str.rfind(sub)       返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1
            str.rindex(sub)      返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误
            str.isalnum()        返回：True， 如果所有的字符都是字母或数字
            str.isalpha()        返回：True，如果所有的字符都是字母
            str.isdigit()        返回：True，如果所有的字符都是数字
            str.istitle()        返回：True，如果所有的词的首字母都是大写
            str.isspace()        返回：True，如果所有的字符都是空格
            str.islower()        返回：True，如果所有的字符都是小写字母
            str.isupper()        返回：True，如果所有的字符都是大写字母
            str.split([sep, [max]])    返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符
            str.rsplit([sep, [max]])   返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符
            str.join(s)                返回：将s中的元素，以str为分割符，合并成为一个字符串。
            str.strip([sub])           返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub
            str.replace(sub, new_sub)  返回：用一个新的字符串new_sub替换str中的sub
            str.capitalize()           返回：将str第一个字母大写
            str.lower()                返回：将str全部字母改为小写
            str.upper()                返回：将str全部字母改为大写
            str.swapcase()             返回：将str大写字母改为小写，小写改为大写
            str.title()                返回：将str的每个词(以空格分隔)的首字母大写
            str.center(width)          返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。
            str.ljust(width)           返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。
            str.rjust(width)           返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。

    - Python小技巧
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


- Python标准库（上）
    - 正则表达式 (re包)
