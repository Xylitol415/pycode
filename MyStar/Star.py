import pygame, sys, random

# 5.设置窗口大小 宽800 高600 后面 参数默认0,0 可不写
screen = pygame.display.set_mode((800, 600), 0, 0)

'''
1. main() --> 设置基本信息
2.action() --> 业务逻辑监听
3.paint() --> 绘制图案
4.init() --> 初始化
'''

'''
图形绘制
1. 绘制一颗星
2. 绘制满天星
3. 绘制动态星星
4. 绘制五颜六色
'''
def paint():
    # 10.设置字体,字体初始化
    pygame.font.init()
    # 11.设置字体样式
    ft = pygame.font.Font("msyhbd.ttc", 28)
    # 12.星星文本

    #wd = ft.render("*", True, (255, 255, 0))
    # 13.绘制星星
    #screen.blit(wd, (100, 100))
    for i in range(0, 100):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        wd = ft.render("★", True, (R, G, B))
        screen.blit(wd, (xx[i], yy[i]))
    # 14.存储星星

xx = []
yy = []
'''
初始化函数
'''
def init():
    # 15.初始化列表
    for i in range(0, 100):
        xx.append(random.randint(0, 800))
        yy.append(random.randint(0, 600))

'''
业务函数
'''
def action():
    # 7.监听退出事件
    #pygame.event.get()获取pygame所有的动作
    for event in pygame.event.get():
        # 8.判断是否退出
        if event.type == pygame.QUIT:
            sys.exit()

'''
满天星 Star
基于pygame
main()
1. 设置窗口标题
2. 设置死循环
3. 设置窗口背景颜色
4. 设置窗口刷新
5. 调整业务逻辑
6. 调整绘制函数
'''
def main():

    # 1. 设置窗口标题
    pygame.display.set_caption("满天星")
    # 2. 循环
    while True:
        # 4.填充背景颜色
        # RGB --->三原色
        screen.fill((0, 0, 0))

        # 6.调用业务逻辑层
        action()

        # 9.调用绘制函数
        paint()

        # 3.刷新屏幕
        pygame.display.update()


if __name__ == '__main__':
    # 16.调用初始化函数
    init()
    main()