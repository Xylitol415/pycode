import pygame
class Bullet(object):
    # 初始化
    def __init__(self, screen, image, x, y):
        # 初始化
        self.screen = screen
        self.image = image
        # 设置子弹发射间隔
        self.interval = 10
        # 获取豌豆的坐标
        self.x = x
        self.y = y

    def shoot(self):
        pass
