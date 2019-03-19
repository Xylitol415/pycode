'''
汤姆猫v2.0
'''
import pygame,sys
class Tom1(object):
    ''' 1.mian() 函数 '''
    def main(self):
        # 1.1设置标题
        pygame.display.set_caption("汤姆猫2.0")
        # 1.2 死循环
        while True:
            # 1.4 业务逻辑执行
            self.action()
            # 1.5 绘制图形
            self.paint()
            # 1.3 刷新屏幕
            pygame.display.update()

    ''' 2. action() '''
    def action(self):
        # 2.1 事件迭代监听
        for event in pygame.event.get():
            # 2.2 退出
            if event.type == pygame.QUIT:
                sys.exit()
            # 2.3 鼠标监听
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 2.4获取鼠标信息
                mouseX, mouseY = pygame.mouse.get_pos()
                # 2.5 获取鼠标点击
                leftFlag = pygame.mouse.get_pressed()[0]
                # 2.6 判断吃鸟动作
                if leftFlag and 30 < mouseX < 90\
                    and 300 < mouseY <360:
                    # 2.7设置图片总数
                    self.count = 40
                    # 2.8 获取图片
                    self.getImage("eat")
                    # 2.9 设置图片集转换值
                    self.index = 0
                # 2.7 判断喝牛奶动作
                elif leftFlag and 30 < mouseX < 90\
                    and 360 < mouseY <420:
                    self.count = 80
                    self.getImage("drink")
                # 2.8 判断敲锣动作
                elif leftFlag and 30 < mouseX < 90\
                    and 420 < mouseY <480:
                    self.count = 12
                    self.getImage("cymbal")
                elif leftFlag and 250 < mouseX < 310\
                    and 300 < mouseY <360:
                    self.count = 27
                    self.getImage("fart")
                elif leftFlag and 250 < mouseX < 310\
                    and 360 < mouseY <420:
                    self.count = 23
                    self.getImage("pie")
                elif leftFlag and 250 < mouseX < 310\
                    and 420 < mouseY <480:
                    self.count = 55
                    self.getImage("scratch")
                elif leftFlag and 90 < mouseX < 200\
                    and 90 < mouseY <250:
                    self.count = 55
                    self.getImage("knockout")
                elif leftFlag and 220 < mouseX < 280\
                    and 400 < mouseY <480:
                    self.count = 25
                    self.getImage("angry")
                elif leftFlag and 100 < mouseX < 180\
                    and 360 < mouseY <420:
                    self.count = 33
                    self.getImage("stomach")
                elif leftFlag and 155 < mouseX < 205\
                    and 470 < mouseY <512:
                    self.count = 29
                    self.getImage("footLeft")
                elif leftFlag and 100 < mouseX < 150\
                    and 470 < mouseY <512:
                    self.count = 29
                    self.getImage("footRight")

    ''' 3. paint()'''
    def paint(self):
        # 3.1绘制背景图片
        self.screen.blit(pygame.transform.scale(self.background, (320, 512)),(0, 0))
        # 3.2 绘制吃鸟动作
        self.screen.blit(self.eat,(30, 300))
        # 3.3 绘制喝牛奶动作
        self.screen.blit(self.drink, (30, 360))
        self.screen.blit(self.cymbal, (30, 420))
        self.screen.blit(self.fart, (250, 300))
        self.screen.blit(self.pie, (250, 360))
        self.screen.blit(self.scratch, (250, 420))
        # 绘制头部




        # 3.3 判断是否运行动画
        # count = -1 index = 0
        if self.count*10 > self.index:
            self.index += 1
            ix = self.index / 10 % len(self.images)
            # 赋值
            self.background = self.images[int(ix)]
        else:
            # 结束清空所有值
            self.count = -1
            self.index = 0
            # 列表的清空
            self.images = []


    ''' 4. init() '''
    def __init__(self):
        # 4.1 背景
        self.screen = pygame.display.set_mode((320, 512),0,0)
        # 4.2 背景图
        self.background = pygame.image.load("Animations/Eat/eat_00.jpg")
        # 4.3 吃鸟的动作
        self.eat = pygame.image.load("Buttons/eat.png")
        # 4.4 图片存储列表
        self.images = []
        # 4.5 图片集转换值
        self.index = 0
        # 4.6 图片数量
        self.count = -1
        # 4.7 喝牛奶
        self.drink = pygame.image.load("Buttons/drink.png")
        # 4.8 敲锣
        self.cymbal = pygame.image.load("Buttons/cymbal.png")
        # 4.9
        self.fart = pygame.image.load("Buttons/fart.png")
        # 4.10
        self.pie = pygame.image.load("Buttons/pie.png")
        # 4.11
        self.scratch = pygame.image.load("Buttons/scratch.png")




    ''' 5. getImage() '''
    def getImage(self, name):
        # 5.1 获取图片
        for i in range(0, self.count):
        # 5.2 判断路径地址
            if i < 10:# name ==> "eat"
                imgPath = "Animations/"+name+"/"+name+"_0"+str(i)+".jpg"
            else:
                imgPath = "Animations/"+name+"/"+name+"_"+str(i)+".jpg"
            # 5.3 存储路径地址
            self.images.append(pygame.image.load(imgPath))

if __name__ == '__main__':
    tm = Tom1()
    tm.main()
