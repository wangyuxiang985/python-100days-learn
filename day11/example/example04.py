"""
写入文件到文本
要将文本信息写入文件文件也非常简单，在使用open函数时指定好文件名并将文件模式设置为'w'即可。
注意如果需要对文件内容进行追加式写入，应该将模式设置为'a'。如果要写入的文件不存在会自动创建文件而不是引发异常。
下面的例子演示了如何将1-9999之间的素数分别写入三个文件中
（1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）
"""
from math import sqrt

def is_prime(n):
    """判断n是否为素数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []

    try:
        for filename in filenames:
            fs_list.append(open(filename, mode='w', encoding='UTF-8'))
        for num in range(1, 10000):
            if is_prime(num):
                if num < 100:
                    fs_list[0].write(str(num) + '\n')
                elif num < 1000:
                    fs_list[1].write(str(num) + '\n')
                else:
                    fs_list[2].write(str(num) + '\n')
    except IOError as ie:
        print(ie)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')


if __name__ == '__main__':
    main()