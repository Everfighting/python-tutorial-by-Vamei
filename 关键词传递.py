# coding=utf-8
def f(a,b,c):
	return a+b+c

print(f(1,2,3))        #默认对应位置传递
print(f(1,c=2,b=2))    #如果对应位置参数正确，则不需要指定。
print(f(b=0,c=1,a=2))  #如果位置与值不对应，则需要明确指定。



