"""
关变量作用域的问题。
Python查找一个变量时会按照“局部作用域”、“嵌套作用域”、“全局作用域”和“内置作用域”的顺序进行搜索
a:全局作用域
b:嵌套作用域
c:局部作用域

“内置作用域”就是Python内置的那些隐含标识符min、len等都属于内置作用域）
"""
def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined
if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()