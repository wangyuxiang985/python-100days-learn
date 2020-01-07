"""
设计一个函数返回给定文件名的后缀名。
"""

def get_suffix(filename, has_hot = False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        if has_hot:
            index = pos
        else:
            index = pos + 1
        return filename[index:]
    else:
        return ''
print(get_suffix("adfddfa.txt"))
print(get_suffix("adfddfa.txt", True))
print(get_suffix("adfddfa"))