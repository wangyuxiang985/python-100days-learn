"""
类之间的关系
类和类之间的关系有三种：is-a、has-a和use-a关系。
is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；
关联关系如果是整体和部分的关联，那么我们称之为聚合关系；
如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），
那么这种就是最强的关联关系，我们称之为合成关系。
use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，
那么司机和汽车的关系就是依赖关系。
"""
class Person(object):
    """父类：人"""
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在观看爱情动作片.' % self._name)
        else:
            print('%s只能观看《熊出没》.' % self._name)

class Student(Person):
    """子类：学生类"""
    __slots__ = ('_name', '_age', '_grade')
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))

class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('骆昊', 38, '老叫兽')
    t.teach('Python程序设计')
    t.watch_av()
    t.age = 16
    t.watch_av()


if __name__ == '__main__':
    main()
