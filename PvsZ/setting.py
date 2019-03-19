'''
setting 小写是文件名
Setting 大写是类名
'''
import pygame


class Setting(object):
    # 初始化变量函数 ==> 加载图片及初始化变量
    def __init__(self):
        # 1. 背景图片
        self.background = pygame.image.load("background1.jpg")
        # 2. 设置卡片图片
        self.cardImages = [
            pygame.image.load("cards/plants/SunFlower.png"),
            pygame.image.load("cards/plants/SunFlowerG.png"),
            pygame.image.load("cards/plants/Peashooter.png"),
            pygame.image.load("cards/plants/PeashooterG.png"),
            pygame.image.load("cards/plants/WallNut.png"),
            pygame.image.load("cards/plants/WallNutG.png"),
        ]
    # 3.获取植物图片方法
    def getPlantsImage(self,count, name, status):
        # 3.1 获取图片
        images = []
        for i in range(0, count):
            # 3.2 判断路径地址
            if i < 10:  # name ==> "eat"
                imgPath = "plants/" + name + "/" + status + "/" + status + "_0" + str(i) + ".png"
            else:
                imgPath = "plants/" + name + "/" + status + "/" + status + "_" + str(i) + ".png"
            # 3.3 存储路径地址
            images.append(pygame.image.load(imgPath))
        return images

    # 4. 获取僵尸图片方法
    def getZombiesImage(self,count, name, status):
        # 4.1 获取图片
        images = []
        for i in range(0, count):
            # 4.2 判断路径地址
            if i < 10:  # name ==> "eat"
                imgPath = "zombies/" + name + "/" + status + "/" + status +"_0" + str(i) + ".png"
            else:
                imgPath = "zombies/" + name + "/" + status + "/" + status + "_" + str(i) + ".png"
            # 4.3 存储路径地址
            images.append(pygame.image.load(imgPath))
        return images