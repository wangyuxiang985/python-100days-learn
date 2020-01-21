"""
读写JSON文件
JSON是“JavaScript Object Notation”的缩写，它本来是JavaScript语言中创建对象的一种字面量语法，
现在已经被广泛的应用于跨平台跨语言的数据交换
使用Python中的json模块就可以将字典或列表以JSON格式保存到文件中
JSON与python对应数据对照关系
JSON	            Python
object	            dict
array	            list
string	            str
number (int / real)	int / float
true / false	    True / False
null	            None
"""

import json

def main():
    mydict = {
        'name': '王二狗',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()