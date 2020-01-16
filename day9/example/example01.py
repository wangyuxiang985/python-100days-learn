"""
面向对象进阶
@property装饰器
之前是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，
使得对属性的访问既安全又方便
"""
class Persion(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    # 访问器@property 相当于getter
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    # 修改器 setter
    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        if self._age < 18:
            print('%s正在完兽旗' % self._name)
        else:
            print('%s正在玩斗地主' % self._name)
def main():
    person = Persion('王二狗', 17)
    person.play()
    person.age = 20
    person.play()
    # AttributeError: can't set attribute
    # person.name = '王大锤'

if __name__ == '__main__':
    main()
