"""
使用Pygame进行游戏开发
Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，其中包含对图像、声音、视频、事件、碰撞等的支持。
Pygame建立在SDL的基础上，SDL是一套跨平台的多媒体开发库，用C语言实现，被广泛的应用于游戏、模拟器、播放器等的开发。
而Pygame让游戏开发者不再被底层语言束缚，可以更多的关注游戏的功能和逻辑。
"""
"""
制作游戏窗口
"""
import pygame

def main():
    # 初始化导入的pygame模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == '__main__':
    main()