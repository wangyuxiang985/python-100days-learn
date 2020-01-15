"""
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
"""
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    def move_to(self, x, y):
        """移动指定位置"""
        self._x = x
        self._y = y
    def move_by(self, dx, dy):
        """移动指定的增量"""
        self._x += dx
        self._y += dy
    def distance_to(self, other):
        """计算与另一个点的距离"""
        dx = self._x - other._x
        dy = self._y - other._y
        return sqrt(dx ** 2 + dy ** 2)
    def __str__(self):
        return '(%s,%s)' % (str(self._x), str(self._y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
