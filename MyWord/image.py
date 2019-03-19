import pygame, sys, random
from pygame.color import THECOLORS
from math import pi

class Image(object):
    def __init__(self):
        self.points = []
        self.screen = pygame.display.set_mode((800, 600), 0, 0)
        self.color_name = random.choice(list(THECOLORS.keys()))
        self.color = THECOLORS[self.color_name]
        #矩形
        self.width = random.randint(0,250)
        self.height = random.randint(0,100)
        self.top = 500
        self.left = 200


    def action(self):
        # 迭代事件监听
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                sys.exit()

    def paint(self):
        # 字体初始化
        pygame.font.init()
        # 设置字体

        # 画圆

        #pygame.draw.circle(self.screen,(255, 255, 255),(200,300), 200, 0)
        #pygame.draw.circle(self.screen,(0, 0, 0),(200,300), 120, 10)
        pygame.draw.circle(self.screen,(255, 255, 255),(400,300), 200, 0)
        pygame.draw.circle(self.screen,(0, 0, 0),(400,300), 200, 10)

        pygame.draw.lines(self.screen,(0, 0, 0),False,[(400,100),(400,150)],10)
        pygame.draw.lines(self.screen,(0, 0, 0),False,[(400,450),(400,500)],10)
        #(Surface, color, Rect, start_angle, stop_angle, width=1)
        #圆内两弧
        pygame.draw.arc(self.screen,(0, 0, 0),[510,130,250, 350],(3*pi)/4, (5*pi)/4,10)
        pygame.draw.arc(self.screen,(0, 0, 0),[35,130,250, 350],(7*pi)/4, pi/4, 10)
        #圆弧两侧横线
        pygame.draw.lines(self.screen,(0, 0, 0),False,[(200,300),(280,300)],10)
        pygame.draw.lines(self.screen,(0, 0, 0),False,[(520,300),(600,300)],10)
        # 画C字
        pygame.draw.rect(self.screen,(0,0,255),(310, 190, 180, 240),0)
        pygame.draw.rect(self.screen,(255,255,255),(328, 208, 145, 200),0)

        pygame.draw.lines(self.screen,(255,255,255),False,[(480,260),(480,350)],25)
        # 画L字
        ftl = pygame.font.Font("msyhbd.ttc", 215)
        wdl = ftl.render("L",True, (255, 0, 0))
        self.screen.blit(wdl, (325, 160))
        # 画A字
        pygame.draw.lines(self.screen,(255,0,0),False,[(415,225),(415,350)],50)

        pygame.draw.lines(self.screen,(255, 255, 255),False,[(415,235),(415,270)],15)
        pygame.draw.lines(self.screen,(255, 255, 255),False,[(415,300),(415,355)],15)

        ft = pygame.font.Font("brushsci.ttf", 40)
        wdl = ft.render("LOS ANGELES CLIPPERS",True, (255, 0, 0))
        self.screen.blit(wdl, (200, 10))

        # 画线
        #pygame.draw.aaline(self.screen,(0, 0, 0),(400,0),(400,600),2)
        #pygame.draw.aaline(self.screen,(0, 0, 0),(0,300),(800,300))
        #pygame.draw.aalines(self.screen,self.color,True, [(400, 0), (0, 580), (780, 580)], 0)
        #pygame.draw.rect(self.screen,(0,0,255),(350, 250, 100, 50),0)
        # 获取鼠标移动得到的点
        #x, y = pygame.mouse.get_pos()
        #self.points.append((x, y))
        #print(self.points)

        # 画点击轨迹图
        #if len(self.points) > 1:
        #    pygame.draw.lines(self.screen, (155, 155, 0), False, self.points, 2)
        #画椭圆
        #pygame.draw.ellipse(self.screen, (0, 255, 0), (0, 0, x, y))
    def main(self):
        # 1.设置标题
        pygame.display.set_caption("洛杉矶快船")
        # 2. 死循环
        while True:

            # 4. 绘制屏幕
            self.screen.fill((255, 255, 255))

            # 5. 业务逻辑
            self.action()

            # 6. 绘制函数
            self.paint()

            pygame.time.delay(5)
            # 3. 刷新屏幕
            pygame.display.update()




if __name__ == '__main__':
    im = Image()
    im.main()