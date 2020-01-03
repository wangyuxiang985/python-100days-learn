"""
使用简单的字符串
"""
def main():

    str1 = 'hello, world!'
    print(len(str1))#字符串长度
    print(str1.capitalize())#首字母大写 副本
    print(str1.upper())#转大写 副本
    print(str1.find('or'))#字串位置
    print(str1.rfind('or'))
    print(str1.find('dfkjd'))#未找到-1
    print(str1.index('or'))#与find一样
    #print(str1.index('sdfk'))#找不到报错
    print(str1)
    print(str1.startswith('he'))#是否以he开头
    print(str1.endswith('!d'))#是否以！d结尾
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))

    str2 = 'abc123456'
    print(str2[2])# 从字符串中取出指定位置的字符(下标运算)
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45

    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())

if __name__ == '__main__':
    main()