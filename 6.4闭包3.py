# coding=utf-8
def line_conf():
	b = 15
	def line(x):
		return 2*x + b
	return line         #return a function object

b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)

# __closure__里包含了一个元组(tuple)。
# 这个元组中的每个元素是cell类型的对象。
# 我们看到的cell包含的就是整数15，也就是我们创建闭包时的环境变量b的取值。





