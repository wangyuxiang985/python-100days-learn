"""
替换字符串中的不良内容

 re模块的正则表达式相关函数中都有一个flags参数，它代表了正则表达式的匹配标记，
 可以通过该标记来指定匹配时是否忽略大小写、是否进行多行匹配、是否显示调试信息等。
 如果需要为flags参数指定多个值，可以使用按位或运算符进行叠加，如flags=re.I | re.M。
"""
import re

def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)  # 你丫是*吗? 我*你大爷的. * you.


if __name__ == '__main__':
    main()