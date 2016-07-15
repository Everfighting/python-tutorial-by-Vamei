# python-tutorial-by-Vamei

- 1.Python基础（上）
    - 添加注释：#!/usr/bin/env python 变成可执行脚本
    - 修改文件权限：chmod 755 hello.py （r:4 w:2 x:1）
    - 执行脚本：./hello.py （仅linux系统）
    - 序列包括：字符串、列表、元组。元组元素不可变，列表元素可变。
    - 短路逻辑(md)：
            举例：not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9
- 2.Python基础（下）
    - 循环：
        - for 元素 in 序列:
                statement
        - while 条件:
                statement
        - 中断条件(py):
                continue 跳过这一环，进行下一环的操作
                break 停止执行整个循环
    - 函数：
        - 值传递

                对于基本数据类型的变量:
                变量传递给函数之后，函数会在内存中复制一个新的变量，从而不影响原来的变量。
        - 指针传递

                对于表来说:
                表传递给函数的是一个指针，指针指向的是序列在内存中的位置，
                在函数中对表的操作将在原有内存中进行，从而影响原有变量。
    - 面向对象的基本概念：
        - 类、属性(py)
        - 方法：具有“行为”的属性(py)
        - 继承：子类享有父类的所有属性(py)

    - 面向对象的进一步拓展:
        - 调用其他信息：通过self，调用类属性：self.laugh(py)
        - __init()__:特殊方法,创建对象时，Python会自动调用这个方法(py)
        - 对象的性质：通过赋值self.attribute，给对象增加新性质(py)
        - 内置函数：dir() 查询类或对象具有属性和 help()查询说明文档

- 3.Python进阶(上)
    - 字典(py)：
        - 创建字典:

                键要求不可变对象（可哈希）。
                键值意义对应。
                字典元素用逗号分隔，没有顺序，无下标。
        - 对字典元素进行循环引用：

                for key in  dict:
                    print dict[key]
        - 字典的其他用法：

                dic.keys()           # 返回dic所有的键
                dic.values()         # 返回dic所有的值
                dic.items()          # 返回dic所有的元素（键值对）
                dic.clear()          # 清空dic，dic变为{}
                del dic['tom']       # 删除 dic 的‘tom’元素（键值对）
                print len(dic)       # 字典中元素个数

    - 文本文件的输入输出:
        - 打开文件

                f = open(文件名，模式)
                模式："r" 只读，"w" 写入，"a"添加

        - 文件对象方法
            - 读取方法：

                    content = f.read(N) #读取N bytes的数据
                    content = f.readline() #读取一样
                    content = f.readlines() #读取所有行，每一行为表中的一个元素
            - 文本写入

                    f.write('I like apple!\n')
            - 关闭文件

                    f.close()
                    with open('/etc/passwd') as f  # 利用上下文管理器自动关闭

        - 循环读入文件：

                for line in file(文件名)：
                    print line

    - 模块(py)：
        - 模块引入方式：

                import a as b             # 引入模块a，并将模块a重命名为b
                from a import function1   # 从模块a中引入function1对象。
                from a import *           # 从模块a中引入所有对象。
                功能相似的模块放在同一个文件夹this_dir里：import this_dir.module
        - 搜索路径：

                - 程序所在的文件夹
                - 操作系统环境变量PYTHONPATH所包含的路径
                - 标准库的安装路径

        - 模块包：

                - 功能相似的模块放在同一个文件夹中
                - 每个文件夹中必须包含__init__.py的文件
                - __init__.py可以是空文件

    - 函数参数传递(py)：

        - 关键字传递：关键字传递是根据每个参数的名字传递参数。
        - 参数默认值：可以给参数赋予默认值。如果该参数最终没有被传递值，将使用该默认值。
        - 包裹传递：参数数量未知时，包裹位置参数，或者包裹关键字参数，在相应元组或字典前加 * 或 * *。
        - 解包裹：解包裹，就是在传递元组时，让元组的每一个元素对应一个位置参数。
        - 基本原则：先位置，再关键字，再包裹位置，再包裹关键字。

- 4.Python进阶（下）

    - 循环设计(py)：
        - range 生成下标
        - enumerate 同时得到下标和元素

                for (index,char) in enumerate(s):
                    print index
                    print char
        - zip 实现并行循环

                ta = [1,2,3]
                tb = ['a','b','c']
                zip(ta,tb) = [(1, 'a'), (2, 'b'), (3, 'c')]
    - 循环对象(py): 包含有一个next()方法的对象
        - 迭代器: 要将循环对象转换成迭代器(iterator)。这一转换是通过使用iter()函数实现的。
        - 生成器(py)：生成器的编写方法和函数定义类似，只是在return的地方改为yield。
        - 表推导(py)：表推导是快速生成表的方法。
    - 函数对象(py)：
        - lambda函数
        - 函数作为参数传递
        - map()函数
        - filter()函数
        - reduce()函数
    - 错误处理：
        - 异常处理(py)：try...except...else...finally
        - 抛出异常：如果无法将异常交给合适的对象，异常将继续向上层抛出，直到被捕捉或者造成主程序报错。
    - 动态类型(py)：
        - 动态类型：

                列表（词典）可以通过引用其元素，改变对象自身。这种对象类型，称为可变数据对象。
                数字和字符串，不能改变对象本身，只能改变引用的指向，称为不可变数据对象。
                元组，不可以赋值，因此不能改变对象自身，所以也算是不可变数据对象。
        - 从动态类型看函数的参数传递：

                本质上传递的是引用。
                如果传递的是可变的对象，改变函数参数，可能改变原对象，指向原对象的引用都会受影响。

- 5.Python深入（上）
    - 特殊方法与多范式

            Python定义的特殊方法使得用户不仅可以使用面向对象的方式编写程序，
            也可以使用面向过程的方式编写相同的功能。
            特殊方法名的前后都用两个下划线。
        - 运算符: 通过调用对象的特殊方法实现的.如'+'做字符串连接。
        - 内置函数：大多也是调用对象的特殊方法.如 len返回表中元素个数。
        - 表元素引用：list[3]即是list.__getitem__(3)。
        - 函数：也是一种对象，即有__call__()特殊方法的对象。
    - 上下文管理器(py)：

            作用：规定某个对象的使用范围。
            方法：一旦进入或者离开该使用范围，会有特殊的操作被调用。
            语法：with...as...
        - 关闭文件：
            with open('new.txt','r') as f 结束后自动调用close方法。

    - 对象的属性：
        - 属性的__dict__系统(py)

                __dict__分层存储属性。
                每一层的__dict__只存储该层新增的属性。
                子类不需要存储父类中的属性。

        - 特性(py)
        - 使用特殊方法__getattr__(py)
        - 即时生成属性的其他方式

- 6.Python深入（下）

    - 闭包:
        - 函数对象的作用域:函数对象存活的范围。
        - 闭包：在Python中一个包含有环境变量取值的函数对象。
        - 闭包与并行运算：通过闭包实现流水线式计算。
    - 装饰器：
        - 装饰函数和方法***(没懂)
        - 含参装饰器
        - 装饰类
    - 内存管理(后续补充)：
        - 对象的内存使用
        - 对象引用对象
        - 引用减少
        - 垃圾回收
        - 分代回收
        - 孤立的引用环

- 7.Python补充
    - 序列的方法
        - 内置函数可用于序列(表，定值表，字符串):

                len(s)         返回： 序列中包含元素的个数
                min(s)         返回： 序列中最小的元素
                max(s)         返回： 序列中最大的元素
                all(s)         返回： True, 如果所有元素都为True的话
                any(s)         返回： True, 如果任一元素为True的话
                sum(s)         返回： 序列中所有元素的和
                s.count(x)     返回： x在s中出现的次数
                s.index(x)     返回： x在s中第一次出现的下标

        - 查询功能函数，不改变序列本身, 可用于表和定值表:

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
        - import模块
        - 查询
            - 查询函数的参数
            - 查询对象的属性
            - 查询对象所属的类和类名称
            - 查询父类

        - 使用中文(以及其它非ASCII编码)
        - 表示2进制，8进制和16进制数字
        - 注释
        - 搜索路径
        - 脚本与命令行结合
        - 安装非标准包

    - Python内置函数清单
        - 数学运算
        - 类型转换
        - 序列操作
        - 类、对象、属性
        - 编译、执行
        - 其他

    - 字符串格式化（%操作符)
        - 模板
        - 格式符


- 8.Python标准库（上）
    - 正则表达式 (re包)
    - 时间与日期 (time, datetime包)
    - 路径与文件 (os.path包, glob包)
    - 文件管理 (部分os包，shutil包)
    - 存储对象 (pickle包，cPickle包)

- 9.Python标准库（中）
    - 子进程 (subprocess包)
    - 信号 (signal包)
    - 多线程与同步 (threading包)
    - 进程信息 (部分os包)
    - 多进程初步 (multiprocessing包)

- 10.Python标准库（下）
    - 多进程探索 (multiprocessing包)
    - 数学与随机数 (math包，random包)
    - 循环器 (itertools)
    - 数据库 (sqlite3)

- 11.Python网络

