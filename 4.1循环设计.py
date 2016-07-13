# coding=utf-8
S = 'abcdefghijk'
for i in range(0,len(S),2):
    print S[i]

# len(string)、range(start,end,step)

S = 'abcdefghijk'
for (index,char) in enumerate(S):
    print index, char

# enumerate自动生成index和list[index]

Ta= [1,2,3]
Tb = [9,8,7]

# cluster

zipped = zip(Ta,Tb)
# Zip对应位置组成元素，形成列表[(1,9),(2,8),(3,7)]
print(zipped)


# decompose
na, nb = zip(*zipped)
# Zip对应位置组成元素，形成列表[(1,2,3),(9,8,7)]
print(na, nb)


ta = [1,2,3]
tb = [9,8,7]
tc = ['a','b','c']
for (a,b,c) in zip(ta,tb,tc):
    print(a,b,c),
