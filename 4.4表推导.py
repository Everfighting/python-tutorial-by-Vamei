# coding=utf-8
L = [x**2 for x in range(10)]
print L

M = [x**2 for x in range(10) if x%2 == 0]
print M

list = ['HELLO', 'World', 'how', 'aRe', 'YOU?']
N = [word.capitalize() for word in list]
n = [word.lower().replace('o','p') for word in list]
print N
print n


xl = [1,3,5]
yl = [9,12,13]
P  = [ x**2 for (x,y) in zip(xl,yl) if y > 10]
print P

