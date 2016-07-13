# coding=utf-8

# 对于字符串，int值采取引用传递
a = 1

def change_integer(a):
	a = a + 1
	return a

print change_integer(a)
print a

print '-'*10

# 对于列表，采取指针传递
b = [1,2,3]

def change_list(b):
	b[0] = b[0] + 1
	return b

print change_list(b)
print b