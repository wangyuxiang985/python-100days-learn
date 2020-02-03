"""
拆分长字符串
"""
import re

def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    re_split = re.split(r'[，。, .]', poem)
    print(re_split) # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡', '']
    print('-------------黄金分割线-----------')
    while '' in re_split:
        re_split.remove('')
    print(re_split) # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

if __name__ == '__main__':
    main()