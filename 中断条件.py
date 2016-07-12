# coding=utf-8
# 跳过2，打印了1~9
for i in range(10):
	if i == 2:
		continue
	print i

print '-'*20

# 只打印了1,2
for j in range(10):
	if j == 2:
		break
	print j
