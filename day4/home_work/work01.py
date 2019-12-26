"""
输入一个正整数判断它是不是素数
"""
import math

num = int(input('请输入一个正整数:'))
end = int(math.sqrt(num))
flag = True
for x in range(2, end + 1):
    if num % x == 0:
        flag = False
        break
if flag and num != 1:
    print('是素数')
else:
    print('%d不是素数,%d是一个因子' % (num, x))