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
        - 装饰函数和方法
        - 含参装饰器
        - 装饰类
    - 内存管理：
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
                以上操作会对表本身产生影响，不是生成新表。

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
            - import TestLib as test # 引用TestLib模块，并将它改名为test
            - from TestLib import lib_func # 只引用TestLib中的lib_func对象，并跳过TestLib引用字段,减少内存占用
            - from TestLib import * # 引用所有TestLib中的对象，并跳过TestLib引用字段
        - 查询
            - 查询函数的参数

                    import inspect
                    print(inspect.getargspec(func))

            - 查询对象的属性

                    除了使用dir()来查询对象的属性之外，还可以使用hasattr函数来确认一个对象是否具有某个属性：
                    a = [1,2,3]
                    print(hasattr(a,'append'))

            - 查询对象所属的类和类名称

                    a = [1, 2, 3]
                    print a.__class__
                    print a.__class__.__name__

            - 查询父类

                    可以用 __base__ 属性来查询某个类的父类：
                    print(list.__base__)

        - 使用中文:

                #coding=utf8
                #-*- coding: UTF-8 -*-

        - 表示2进制，8进制和16进制数字

                print(0b1110)     # 二进制，以0b开头
                print(0o10)       # 八进制，以0o开头
                print(0x2A)       # 十六进制，以0x开头

        - 注释

                一行内的注释可以以#开始。
                多行的注释可以以'''开始，以'''结束

        - 搜索路径

                当我们import的时候，Python会在搜索路径中查找模块(module)。
                shell中增加PYTHONPATH环境变量:
                $export PYTHONPATH=$PYTHONPATH:/home/vamei/mylib

        - 脚本与命令行结合

                在脚本运行结束后，直接进入Python命令行。
                $python -i script.py

        - 安装非标准包

                (1)、使用Linux repository (Linux环境)
                (2)、使用pip
                        $pip install -i http://mirrors.aliyuncs.com/pypi/simple web.py
                        $pip uninstall web.py
                        $pip install -i http://mirrors.aliyuncs.com/pypi/simple --upgrade web.py
                (3)、从源码编译

    - Python内置函数清单
        - 数学运算

                abs(-5)                          # 取绝对值，也就是5
                round(2.6)                       # 四舍五入取整，也就是3.0
                pow(2, 3)                        # 相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
                cmp(2.3, 3.2)                    # 比较两个数的大小
                divmod(9,2)                      # 返回除法结果和余数
                max([1,5,2,9])                   # 求最大值
                min([9,2,-4,2])                  # 求最小值
                sum([2,-1,9,12])                 # 求和

        - 类型转换

                int("5")                         # 转换为整数 integer
                float(2)                         # 转换为浮点数 float
                long("23")                       # 转换为长整数 long integer
                str(2.3)                         # 转换为字符串 string
                complex(3, 9)                    # 返回复数 3 + 9i

                ord("A")                         # "A"字符对应的数值
                chr(65)                          # 数值65对应的字符
                unichr(65)                       # 数值65对应的unicode字符

                bool(0)                          # 转换为相应的真假值，在Python中，0相当于False .在Python中，下列对象都相当于False：** [], (), {}, 0, None, 0.0, '' **

                bin(56)                          # 返回一个字符串，表示56的二进制数
                hex(56)                          # 返回一个字符串，表示56的十六进制数
                oct(56)                          # 返回一个字符串，表示56的八进制数

                list((1,2,3))                    # 转换为表 list
                tuple([2,3,4])                   # 转换为定值表 tuple
                slice(5,2,-1)                    # 构建下标对象 slice
                dict(a=1,b="hello",c=[1,2,3])    # 构建词典 dictionary

        - 序列操作

                all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
                any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值

                sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
                reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]

        - 类、对象、属性

                hasattr(me, "test")               # 检查me对象是否有test属性
                getattr(me, "test")               # 返回test属性
                setattr(me, "test", new_test)     # 将test属性设置为new_test
                delattr(me, "test")               # 删除test属性
                isinstance(me, Me)                # me对象是否为Me类生成的对象 (一个instance)
                issubclass(Me, object)            # Me类是否为object类的子类

        - 编译、执行

                repr(me)                          # 返回对象的字符串表达
                compile("print('Hello')",'test.py','exec')       # 编译字符串成为code对象
                eval("1 + 1")                     # 解释字符串表达式。参数也可以是compile()返回的code对象
                exec("print('Hello')")            # 解释并执行字符串，print('Hello')。参数也可以是compile()返回的code对象

        - 其他

                input("Please input:")            # 等待输入

                globals()                         # 返回全局命名空间，比如全局变量名，全局函数名
                locals()                          # 返回局部命名空间

    - 字符串格式化（%操作符)
        - 模板

                print("I'm %s. I'm %d year old" % ('Vamei', 99))
                a = "I'm %s. I'm %d year old" % ('Vamei', 99)
                print (a)
                print("I'm %(name)s. I'm %(age)d year old" % {'name':'Vamei', 'age':99})

        - 格式符

                %s    字符串 (采用str()的显示)
                %r    字符串 (采用repr()的显示)
                %c    单个字符
                %b    二进制整数
                %d    十进制整数
                %i    十进制整数
                %o    八进制整数
                %x    十六进制整数
                %e    指数 (基底写为e)
                %E    指数 (基底写为E)
                %f    浮点数
                %F    浮点数，与上相同
                %g    指数(e)或浮点数 (根据显示长度)
                %G    指数(E)或浮点数 (根据显示长度)

                %%    字符"%"

        - 格式符进阶

                %[(name)][flags][width].[precision]typecode
                举例：
                print("%+10x" % 10)
                print("%04d" % 5)
                print("%6.3f" % 2.3)

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
    -原始Python服务器

        TCP/IP和socket
        TCP socket
        基于TCP socket的HTTP服务器
        深入HTTP服务器程序
        使用浏览器实验
        探索的方向

    -Python服务器进化

        支持POST
        使用SocketServer
        SimpleHTTPServer: 使用静态文件来回应请求
        CGIHTTPServer：使用静态文件或者CGI来回应请求

