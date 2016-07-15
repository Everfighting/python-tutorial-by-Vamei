# coding=utf-8
def line_conf(a,b):
	def line(x):
		return a*x+b
	return line
line1 = line_conf(1,1)
line2 = line_conf(4,5)
print(line1(5),line2(5))

# 闭包可以提高代码的可复用性
# 只需变换参数a,b,就可以获得不同的直线表达式
