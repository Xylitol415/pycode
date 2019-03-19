'''
汤姆猫v2.0
'''
import pygame,sys
from peashooter import peaShooter
from setting import Setting

class PvsZ(object):
    ''' 1.mian() 函数 '''
    def main(self):
        # 1.1设置标题
        pygame.display.set_caption("植物大战僵尸")
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
                for i in range(10):
                    if leftFlag and 100< mouseX < 250\
                        and 100 < mouseY <250:
                        # 2.8 制定区域创建豌豆对象
                        self.peashooter.append(peaShooter(self.screen, self.peaImage, 200+i*50, 200+i*50))
                        # 2.9 设置图片集转换值
                        self.index = 0
        self.change()

    # 变化业务逻辑执行
    def change(self):
        for pea in self.peashooter:
            pea.change()

    ''' 3. paint()'''
    def paint(self):
        # 3.1绘制背景图片
        self.screen.blit(pygame.transform.scale(self.background, (1200, 600)),(0, 0))
        self.paintPeashooter()

    # 画豌豆
    def paintPeashooter(self):
        for pea in self.peashooter:
            pea.blitMe()


    ''' 4. init() '''
    def __init__(self):
        # 4.1 背景
        self.screen = pygame.display.set_mode((906, 601),0,0)
        self.sets = Setting()
        # 4.2 背景图
        self.background = self.sets.background

        # 创建豌豆对象
        self.peaImage = self.sets.getPlantsImage(7, "peashooter", "idle")
        self.peashooter = []


if __name__ == '__main__':
    pvsz = PvsZ()
    pvsz.main()
