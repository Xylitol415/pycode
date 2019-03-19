'''
炸弹类
'''
from nexonObject import NexonObject

class Bomb(NexonObject):
    # 类初始化函数
    def __init__(self, screen, image, x, y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        super(Bomb, self).__init__(screen, self.image, self.x, self.y)
        # 设置炸弹生存时间
        self.live = 10

    #  更改生命值
    def updateLive(self):
        self.live -= 1
    # 抽象函数
    def outOfBounds(self, dir):
        pass