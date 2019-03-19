'''
bao
1. init 函数
2. step() 走一步
3. outOfBounds() 判断手抖出界
'''
from nexonObject import NexonObject
import pygame

class Bao(NexonObject):
    # 初始化
    def __init__(self, screen, images):
        # 初始化
        self.screen = screen
        self.images = images
        # 上下左右
        self.image = self.images[1]
        # 坐标  详细坐标点
        self.x = 13
        self.y = 0
        # 调用父类构造函数
        super(Bao, self).__init__(screen, self.image, self.x, self.y)
        # 设置泡泡数量
        self.number = 1
        # 设置泡泡的威力
        self.power = 2


    def outOfBounds(self,dir):
        # 根据移动方向 预判下一步是否出界
        if dir == 0:
            # 如果下一步在该区间内 可以移动
            return 0<= self.y-1 < 13
        elif dir == 1:
            return 0<= self.y+1 < 13
        elif dir == 2:
            return 0 <= self.x-1 < 15
        elif dir == 3:
            return 0 <= self.x+1 < 15


    # 走一步
    def step(self,dir,build):
        # 判断 方向 出界  建筑物
        if dir == 0 and self.outOfBounds(dir) and self.judgeBuild(dir,build):
            self.y -= 1
            self.image = self.images[0]

        elif dir == 1 and self.outOfBounds(dir) and self.judgeBuild(dir,build):
            self.y += 1
            self.image = self.images[1]

        elif dir == 2 and self.outOfBounds(dir) and self.judgeBuild(dir,build):
            self.x -= 1
            self.image = self.images[2]

        elif dir == 3 and self.outOfBounds(dir) and self.judgeBuild(dir,build):
            self.x += 1
            self.image = self.images[3]

    # 判断建筑物
    def judgeBuild(self, dir,  build):
        # 预判下一步的建筑物是什么类型
        if dir == 0 and self.outOfBounds(dir):
            # 6-->空白
            return build[self.y-1][self.x] == 6

        elif dir == 1 and self.outOfBounds(dir):
            return build[self.y+1][self.x] == 6

        elif dir == 2 and self.outOfBounds(dir):
            return build[self.y][self.x-1] == 6

        elif dir == 3 and self.outOfBounds(dir):
            return build[self.y][self.x+1] == 6
