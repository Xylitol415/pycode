'''
豌豆类

'''
import pygame
class peaShooter(object):
    # 初始化
    def __init__(self, screen, images, x, y):
        # 初始化
        self.screen = screen
        self.images = images
        # 获取豌豆的图片
        self.image = self.images[0]
        # 设置生命值
        self.live = 10
        # 获取豌豆的坐标
        self.x = x
        self.y = y
        # 属性
        # 图片集转换值
        self.index = 0

    # 豌豆图片动态转换
    def change(self):
        # 1.改变图片集转换值
        self.index += 1
        # 2. 根据图片集转换值修改变量频率
        ix = self.index / 10 % len(self.images)
        # 根据频率x修改图片 ix 必须为int类型
        self.image = self.images[int(ix)]

    # 更改生命值
    def updateLive(self):
        self.live -= 1

    # 绘制函数
    def blitMe(self):
        self.screen.blit(self.image, (self.x, self.y))