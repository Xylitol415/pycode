'''

Tomcat
1. 搭建窗口信息

'''
import pygame,sys

class Tom(object):
    ''' 1. main() 窗口基本注释 '''
    def main(self):
        # 1.1设置窗口标题
        pygame.display.set_caption('汤姆猫',)
        # 1.2设置死循环
        while True:
            # 1.4 业务逻辑执行
            self.action()
            # 1.5 图形图片绘制
            self.paint()
            # 1.3 更新屏幕
            pygame.display.update()


    ''' 2. action函数  业务逻辑处理 '''
    def action(self):
        # 2.1 事件监听迭代
        for event in pygame.event.get():
            # 2.2 判断事件类型
            if event.type == pygame.QUIT:
                sys.exit()
            # 2.3 鼠标单击
            mouseX, mouseY = pygame.mouse.get_pos()
            # 获取鼠标单击事件
            # [0] 左键单击 [1] 左键双击 [2] 右击
            leftFlag = pygame.mouse.get_pressed()[0]
            # 2.4 判断
            if leftFlag and 30 < mouseX < 30+60 \
                and 300 < mouseY < 300 + 60:
                # 吃鸟的动作
                #print("进入了")
                self.animation = 0
                # 重新设置index
                self.index = 0
            elif leftFlag and 30 < mouseX < 30+60 \
                and 370 < mouseY < 370 + 60:
                self.animation = 1
                self.index = 0
            elif leftFlag and 30 < mouseX < 30+60 \
                and 440 < mouseY < 440 + 60:
                self.animation = 2
                self.index = 0
            elif leftFlag and 250 < mouseX < 250+60 \
                and 300 < mouseY < 300 + 60:
                self.animation = 3
                self.index = 0
            elif leftFlag and 250 < mouseX < 250+60 \
                and 370 < mouseY < 370 + 60:
                self.animation = 4
                self.index = 0
            elif leftFlag and 250 < mouseX < 250+60 \
                and 440 < mouseY < 440 + 60:
                self.animation = 5
                self.index = 0
            #....未完
            elif leftFlag and 250 < mouseX < 250+60 \
                and 440 < mouseY < 440 + 60:
                self.animation = 6
                self.index = 0


    ''' 3. paint函数 绘制图形'''
    def paint(self):

        # 3.6 判断是否执行动画效果
        if self.animation == 0:
            # 3.2 图片集转换值增加
            self.index += 1
            # 3.3 设置图片转换频率
            # index 0/10 ==> 0 % 10 ==> 0
            # index 1/10 ==> 0 % 10 ==> 0
            # ...
            # index 11/10 ==> 1 % 10 ==> 1
            # ix = 0 0 0 0 0 0 0 0 0 0 1
            # ix 每调用一次函数 10次才会刷新一次
            ix = self.index / 10 % len(self.eats)
            # 3.4 重新赋值图片 ix --> float
            self.background = self.eats[int(ix)]
            # 判断是否是最后一张
            if int(ix) == 39:
                self.animation = -1
        elif self.animation == 1:
            self.index += 1
            ix = self.index / 10 % len(self.drinks)
            self.background = self.drinks[int(ix)]
            if int(ix) == 79:
                self.animation = -1
        elif self.animation == 2:
            self.index += 1
            ix = self.index / 30 % len(self.cymbals)
            self.background = self.cymbals[int(ix)]
            if int(ix) == 11:
                self.animation = -1
        elif self.animation == 3:
            self.index += 1
            ix = self.index / 10 % len(self.farts)
            self.background = self.farts[int(ix)]
            if int(ix) == 26:
                self.animation = -1
        elif self.animation == 4:
            self.index += 1
            ix = self.index / 10 % len(self.pies)
            self.background = self.pies[int(ix)]
            if int(ix) == 22:
                self.animation = -1
        elif self.animation == 5:
            self.index += 1
            ix = self.index / 10 % len(self.scratchs)
            self.background = self.scratchs[int(ix)]
            if int(ix) == 54:
                self.animation = -1
        elif self.animation == 6:#头
            self.index += 1
            ix = self.index / 10 % len(self.angrys)
            self.background = self.angrys[int(ix)]
            if int(ix) == 24:
                self.animation = -1
        elif self.animation == 7:#肚子
            self.index += 1
            ix = self.index / 10 % len(self.stomachs)
            self.background = self.stomachs[int(ix)]
            if int(ix) == 32:
                self.animation = -1
        elif self.animation == 8:#尾巴
            self.index += 1
            ix = self.index / 10 % len(self.knockouts)
            self.background = self.knockouts[int(ix)]
            if int(ix) == 79:
                self.animation = -1
        elif self.animation == 9:#左脚
            self.index += 1
            ix = self.index / 10 % len(self.footLefts)
            self.background = self.stomachs[int(ix)]
            if int(ix) == 28:
                self.animation = -1
        elif self.animation == 10:#右脚
            self.index += 1
            ix = self.index / 10 % len(self.footRights)
            self.background = self.footRights[int(ix)]
            if int(ix) == 28:
                self.animation = -1

        # 3.1 绘制背景图片
        self.screen.blit(pygame.transform.scale(self.background,(320, 512)), (0, 0))
        # 3.5 绘制吃鸟动作
        self.screen.blit(self.eat, (30, 300))
        self.screen.blit(self.drink, (30, 370))
        self.screen.blit(self.cymbal, (30, 440))
        self.screen.blit(self.fart, (250, 300))
        self.screen.blit(self.pie, (250, 370))
        self.screen.blit(self.scratch, (250, 440))
        #self.screen.blit(self.angry, (250, 440))
        #self.screen.blit(self.stomach, (250, 440))
        #self.screen.blit(self.knockout, (250, 440))
        #self.screen.blit(self.footLeft, (250, 440))
        #self.screen.blit(self.footRights, (250, 440))




    ''' 4.__init__ 函数 属性初始化'''
    def __init__(self):
        # 窗口大小设置
        self.screen = pygame.display.set_mode((320, 512), 0, 0)
        # 背景图片
        self.background = pygame.image.load("Animations/Eat/eat_00.jpg")
        # 图片列表存储
        self.eats = self.getImage("Animations/Eat/eat_0", "Animations/Eat/eat_", ".jpg", 40)
        self.drinks = self.getImage("Animations/Drink/drink_0","Animations/Drink/drink_",".jpg", 80)
        self.cymbals = self.getImage("Animations/Cymbal/cymbal_0", "Animations/Cymbal/cymbal_", ".jpg", 12)
        self.farts = self.getImage("Animations/Fart/fart_0", "Animations/Fart/fart_", ".jpg", 27)
        self.pies = self.getImage("Animations/Pie/pie_0", "Animations/Pie/pie_", ".jpg", 23)
        self.scratchs = self.getImage("Animations/Scratch/scratch_0", "Animations/Scratch/scratch_", ".jpg", 55)
        self.angrys = self.getImage("Animations/Angry/angry_0", "Animations/Angry/angry_", ".jpg", 25)
        self.stomachs = self.getImage("Animations/Stomach/stomach_0", "Animations/Stomach/stomach_", ".jpg", 33)
        self.knockouts = self.getImage("Animations/Knockout/knockout_0", "Animations/Knockout/knockout_", ".jpg", 80)
        self.footLefts = self.getImage("Animations/FootLeft/footLeft_0", "Animations/FootLeft/footLeft_", ".jpg", 29)
        self.footRights = self.getImage("Animations/FootRight/footRight_0", "Animations/FootRight/footRight_", ".jpg", 29)
        # 图片集转换值
        self.index = 0
        # 吃鸟
        self.eat = pygame.image.load("Buttons/eat.png")
        # 判断动画动作
        self.animation = -1
        # 喝奶
        self.drink = pygame.image.load("Buttons/drink.png")
        self.cymbal = pygame.image.load("Buttons/cymbal.png")
        self.fart = pygame.image.load("Buttons/fart.png")
        self.pie = pygame.image.load("Buttons/pie.png")
        self.scratch = pygame.image.load("Buttons/scratch.png")



    ''' 5. getImage() 获取图片列表'''
    def getImage(self,prePath1, prePath2, endPath, picNum):
        # 5.4 定义列表
        imageList = []
        # 5.1 循环迭代赋值图片
        for i in range(0, picNum):
            # 5.2 获取图片路径
            if i < 10:
                imgPath = prePath1 + str(i) + endPath
            else:
                imgPath = prePath2 + str(i) + endPath
            # 5.3 返回列表
            imageList.append(pygame.image.load(imgPath))
        # 5.5 返回
        return imageList

if __name__ == '__main__':
    # 获取类
    tm = Tom()
    # 调用类方法
    tm.main()