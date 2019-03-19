'''
1. 设置窗口
2. 设置监听
3. 绘制星星
4. 绘制满天星
'''


import pygame, sys,random

class Star(object):
    # 初始化函数
    def __init__(self):
        self.screen =  pygame.display.set_mode((800, 600), 0, 0)
        self.xx = []
        self.yy = []
        #100 颗星星
        for i in range(0, 100):
            self.xx.append(random.randint(0, 800))
            self.yy.append(random.randint(0, 600))
    # 绘制图形图案
    def paint(self):

        # 画圆
        # screen --> 画在哪里
        # (255, 255, 0) --> 颜色值
        # (100, 100) --> 圆的圆心点
        # 50 --> 圆的半径
        # 0 --> 圆是否填充 0填充 其他数字：边的宽度
        pygame.draw.circle(self.screen,(255, 255, 0),(100,100), 50, 0)
        # 用背景黑色画小圆覆盖在大圆上 形成月牙
        pygame.draw.circle(self.screen,(0, 0, 0),(80,80), 50, 0)

        # 画线
        pygame.draw.aaline(self.screen,(255, 255, 0),(300,300),(200,200))

        # 字体初始化
        pygame.font.init()
        # 设置字体
        ft = pygame.font.Font("msyhbd.ttc", 28)
        # 设置绘制内容
        #wd = ft.render("★", True, (255,255,255))
        # 窗口绘制
        #self.screen.blit(wd, (100,100))
        for i in range(0, 100):
            R = random.randint(0, 255)
            G = random.randint(0, 255)
            B = random.randint(0, 255)
            wd = ft.render("★", True, (R,G,B))
            self.screen.blit(wd, (self.xx[i], self.yy[i]))
    # 业务逻辑处理方法
    def action(self):
        # 事件监听迭代
        for event in pygame.event.get():
            # 判断
            if event.type == pygame.QUIT:
                sys.exit()
        # 星星的移动
        for i in range(0, 100):
            self.xx[i] += 1
            self.yy[i] += 1
            # 移动的循环
            if self.xx[i] > 800:
                self.xx[i] = 0
            if self.yy[i] > 600:
                self.yy[i] = 0

    def main(self):
        # 1. 设置窗口标题
        pygame.display.set_caption("满天星")
        # 2.死循环
        while True:
            # 4.窗口填充
            self.screen.fill((0, 0, 0))
            '''
            for i in range(0, 100):
                R = random.randint(0, 255)
                G = random.randint(0, 255)
                B = random.randint(0, 255)
            self.screen.fill((R, G, B))
            '''
            # 5. 业务层
            self.action()
            # 6. 绘制
            self.paint()
            # 7.调整刷新的频率
            pygame.time.delay(10)
            # 3. 刷新屏幕
            pygame.display.update()


if __name__ == '__main__':
    st = Star()
    st.main()