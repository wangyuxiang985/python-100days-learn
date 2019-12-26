"""
输出乘法口诀表(九九表)
end='\t' 每一个输出以一个制表符结束，默认每一个输出以换行符结束
"""
for x in range(1, 10):
    for y in range(1, x + 1):
        print('%d * %d = %d' % (x, y, x * y), end='\t')
    print()