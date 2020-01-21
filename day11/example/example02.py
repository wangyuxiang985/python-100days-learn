"""
读写文本文件
读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）
并将文件模式设置为'r'（如果不指定，默认值也是'r'），
然后通过encoding参数指定编码（如果不指定，默认值是None，那么在读取文件时使用的是操作系统默认的编码），
如果不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，
那么就可能因无法解码字符而导致读取失败
"""

def main():
    """
    如果open函数指定的文件并不存在或者无法打开，那么将引发异常状况导致程序崩溃
    FileNotFoundError: [Errno 2] No such file or directory: '致橡树.txt'
    """
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()