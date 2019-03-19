'''
父类
'''
# abc 抽象方法定义
import pygame,abc

class NexonObject(object):
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
    # 抽象函数
    @abc.abstractmethod
    def outOfBounds(self, dir):
        pass
    # 图形绘制
    def blitMe(self):
        self.screen.blit(self.image, (25+self.x*50, 25+self.y*50))