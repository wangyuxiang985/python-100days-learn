"""
碰撞检测
通常一个游戏中会有很多对象出现，而这些对象之间的“碰撞”在所难免，比如炮弹击中了飞机、箱子撞到了地面等。
碰撞检测在绝大多数的游戏中都是一个必须得处理的至关重要的问题，
pygame的sprite（动画精灵）模块就提供了对碰撞检测的支持，
这里我们暂时不介绍sprite模块提供的功能，因为要检测两个小球有没有碰撞其实非常简单，
只需要检查球心的距离有没有小于两个球的半径之和。为了制造出更多的小球，我们可以通过对鼠标事件的处理，
在点击鼠标的位置创建颜色、大小和移动速度都随机的小球，当然要做到这一点，
我们可以把之前学习到的面向对象的知识应用起来。
"""
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame


@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):
    """球类"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self.alive = True

    def move(self, screen):
        """"移动"""
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 or \
                self._x + self._radius >= screen.get_width():
            self._sx = -self._sx
        if self._y - self._radius <= 0 or \
                self._y + self._radius >= screen.get_height():
            self._sy = -self._sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            _dx, _dy = self._x - other._x, self._y - other._y
            distance = sqrt(_dx ** 2 + _dy ** 2)
            if distance < self._radius + other._radius \
                    and self._radius > other._radius:
                other.alive = False
                self._radius = self._radius + int(other._radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self._color,
                           (self._x, self._y), self._radius, 0)

