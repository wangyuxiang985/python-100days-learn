"""
使用简单的列表
list = [列表] 可变
t = (元组) 不可变
set = {集合} 不重复
scores = {'key':value} 字典
"""
def main():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = ['hello'] * 5
    print(list2)
    list3 = 'hello' * 5
    print(list3)

    # 计算列表长度(元素个数)
    print(len(list1))
    # 下标(索引)运算
    print(list1[0])
    print(list1[4])
    #print(list1[5])  # IndexError: list index out of range
    print(list1[-1])
    print(list1[-3])
    print(list1[-5])
    #print(list1[-6]) #IndexError: list index out of range
    list1[2] = 300
    print(list1)

    #添加元素
    list1.append(200)
    list1.append(200)
    print(list1)
    list1.insert(1, 666)
    print(list1)
    list1 += [111, 222]
    print(list1)

    list1.remove(200)#删除遇到的第一个 不存在报错
    print(list1)
    if 1234 in list1:
        list1.remove(1234)
    #list1.remove(1234) #ValueError: list.remove(x): x not in list
    del list1[1]
    print(list1)
    list1.clear()
    print(list1)
    print(len(list1))
if __name__ == '__main__':
    main()