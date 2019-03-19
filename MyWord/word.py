'''
键盘监听事件

1. 生成字符
2. 绘制字符
3. 移动字符
4. 键盘监听比对
5. 得分
6. 删除

#课堂练习
1. 字符  只有一个颜色 删除后会更改颜色
2. 得分 击中一个字符 10 显示在界面上 字母到底-10分
3. 根据得分 控制速度
    0 < score < 100 速度为10
    100 < score < 200 速度为5
    200 < score < 300 速度1

4. Game over
    # 1. init --> self.flag == True
    # 2. action() --> 判断分数下方 -->
    if self.score < 0:
        self.flag = False
    # 3. While Ture: --> While self.flag
    # 4. paint() --> 显示分数
    if self.flag == False:
        game = ft.render("GAME OVER !", True, (255,0,0))
        self.screen.blit(game,(400, 300))

'''

import pygame, sys, random

class Word(object):

    '''初始化函数'''
    def __init__(self):
        # 屏幕
        self.screen = pygame.display.set_mode((800, 600), 0, 0)
        # 生成字符和字符的坐标点
        self.word = []
        self.xx = []
        self.yy = []
        self.colors = []
        # 分数
        self.score = 0
        # 速度
        self.speed = 10
        # 游戏结束标志
        self.flag = True
        # 赋值
        for i in range(0, 10):
            self.xx.append(random.randint(0, 800))
            self.yy.append(-random.randint(0, 600))
            # A-Z 左闭右开
            self.word.append(random.randint(65, 90))
            # 颜色存储()
            # 元组
            self.colors.append(self.getColor())
    '''
    业务处理
    '''
    def action(self):
        # 迭代事件监听
        for event in pygame.event.get():
            # 判断事件类型
            if event.type == pygame.QUIT:
                sys.exit()
            # 判断监听事件
            if event.type == pygame.KEYDOWN:
                # 逐个比对
                for i in range(len(self.word)):
                    # word[] 大写
                    wd = self.word[i]
                    if wd + 32 == event.key:
                        # 删除 --> 重新填充
                        #del self.word[i]
                        self.word[i] = random.randint(65, 90)
                        # 修改坐标
                        self.xx[i] = random.randint(0, 800)
                        self.yy[i] = -random.randint(0, 600)
                        # 重新生成一个颜色
                        self.colors[i] = self.getColor()
                        # 计算得分
                        self.score += 10
                        # 非常重要的代码
                        break


        # 字符移动
        for i in range(0, 10):
            if(self.flag):
                self.yy[i] += 1
            # 判断循环
            if self.yy[i] > 600:
                # 减分
                self.score -= 10
                self.yy[i] = 0

        # 判断速度
        if 0 <= self.score < 100:
            self.speed = 10
        elif 100 <= self.score < 200:
            self.speed = 5
        elif 200 <= self.score < 300:
            self.speed = 1
        else:
            self.flag = False

    '''
    绘制函数
    '''
    def paint(self):
        # 字体初始化
        pygame.font.init()
        # 设置字体
        ft = pygame.font.Font("msyhbd.ttc", 24)
        # 显示得分
        ScoreWd = ft.render("得分:%d" % self.score, True, (255,255,0))
        self.screen.blit(ScoreWd, (675, 25))
        # 设置绘制内容
        for i in range(0, 10):
            # 绘制的内容
            wd = ft.render(chr(self.word[i]), True, self.colors[i])
            # 屏幕绘制
            self.screen.blit(wd, (self.xx[i], self.yy[i]))
        # 设置结束
        if self.flag == False:
            game = ft.render("GAME OVER !", True, (255,0,0))
            self.screen.blit(game,(400, 300))


    def getColor(self):
        color = []
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        color.append(R)
        color.append(G)
        color.append(B)
        return tuple(color)



    '''
    设置窗口
    '''
    def main(self):
        # 1.设置标题
        pygame.display.set_caption("打字游戏")
        # 2.死循环
        #while True:
        while self.flag:
            # 4.绘制屏幕
            self.screen.fill((233, 233, 233))
            # 5.业务处理
            self.action()
            # 6.绘制函数
            self.paint()
            # 10. 调整速度
            pygame.time.delay(self.speed)

            # 3.更新屏幕
            pygame.display.update()


if __name__ == '__main__':
    wd = Word()
    wd.main()