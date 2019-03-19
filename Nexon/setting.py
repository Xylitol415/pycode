'''
setting 小写是文件名
Setting 大写是类名
'''
import pygame


class Setting(object):
    # 初始化变量函数 ==> 加载图片及初始化变量
    def __init__(self):
        # 1. 背景图片
        self.background = pygame.image.load("img/zhan2.jpg")
        # 2. 设置地板
        self.diban1 = pygame.image.load("img/diban1.png")
        self.diban2 = pygame.image.load("img/diban2.png")
        self.diban3 = pygame.image.load("img/diban3.png")
        self.diban4 = pygame.image.load("img/diban4.png")
        # 3. 设置地板图
        self.floor = [
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 3, 4, 3, 1, 1, 1, 1, 1, 1]
                    ]
        # 4.设置建筑物图片
        self.shu = pygame.image.load("img/shu.png")
        self.red = pygame.image.load("img/red.png")
        self.orange = pygame.image.load("img/orange.png")
        self.redHouse = pygame.image.load("img/redHouse.png")
        self.blueHouse = pygame.image.load("img/blueHouse.png")
        self.yellowHouse = pygame.image.load("img/yellowHouse.png")
        self.box = pygame.image.load("img/box.png")

        # 5. 设置宝宝图片
        self.baoImages = [
            pygame.image.load("img/up.png"),
            pygame.image.load("img/down.png"),
            pygame.image.load("img/left.png"),
            pygame.image.load("img/right.png")
        ]
        # 6. 泡泡的图片
        self.paoImages = [
            pygame.image.load("img/PP1.png"),
            pygame.image.load("img/PP2.png")
        ]
        # 7. 炸弹图片
        self.bombImages = [
            pygame.image.load("img/bombUp.png"),
            pygame.image.load("img/Bombing.png")
        ]