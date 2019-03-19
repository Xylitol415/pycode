'''
泡泡堂
1.设置窗口基本信息
2. 绘制地板
3. 绘制地图
4. 宝宝类
    4.1 nexonObject ==> NexonObject
    4.2 属性 screen, image, x, y
    4.3 公共函数 outOfBounds() ==>  出界判断
    4.4 bao ==> Bao

5. 宝宝移动
    5.1 宝宝 action() 键盘监听
    5.2 宝宝自定义函数 step()
6. 宝宝放泡
    6.1 pao ===> 泡泡的类
    6.2 泡泡的生成

7. 炸弹制作
    7.1 bomb ==> 炸弹类
    7.2 炸弹的生成
8. 建筑物销毁
    8.1 change() 2部分 炸弹变化
9. 根据泡泡数量放置泡泡
    9.1 bao ==> self.number
10. 根据泡泡的威力生成炸弹
    10.1 ===> self.power

'''
# 导入
import pygame, sys
from setting import Setting
from bao import Bao
from pao import Pao
from bomb import Bomb

class PPTGame(object):
    '''第一区域：属性初始化'''
    def __init__(self):
        # 1.1 屏幕
        self.screen = pygame.display.set_mode((925, 700), 0, 0)
        # 1.2 获取设置文件
        self.sets = Setting()
        # 1.3 设置建筑物
        '''建筑物
        树 0
        红色方块 1 
        橙色方块 2
        红房子 3
        蓝房子 4
        黄房子 5
        空白 6
        箱子 7
        树丛 6 
        '''
        self.build = [
            [6, 2, 1, 2, 1, 0, 6, 6, 7, 0, 5, 1, 5, 6, 5],
            [6, 3, 7, 3, 7, 0, 7, 6, 6, 0, 1, 2, 6, 6, 6],
            [6, 6, 1, 2, 1, 0, 6, 7, 7, 0, 5, 7, 5, 7, 5],
            [7, 5, 7, 5, 7, 0, 7, 6, 6, 0, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 0, 6, 6, 7, 0, 5, 7, 5, 7, 5],
            [2, 3, 2, 3, 2, 3, 7, 7, 6, 6, 1, 2, 1, 2, 1],
            [0, 0, 0, 0, 0, 0, 6, 6, 7, 0, 0, 0, 0, 0, 0],
            [1, 2, 1, 2, 1, 6, 7, 6, 6, 0, 1, 3, 1, 3, 6],
            [4, 7, 4, 7, 4, 0, 6, 7, 7, 0, 1, 2, 1, 6, 6],
            [2, 1, 2, 1, 2, 0, 7, 6, 6, 0, 7, 3, 7, 3, 6],
            [4, 2, 4, 7, 4, 0, 6, 6, 7, 0, 1, 2, 1, 2, 6],
            [6, 2, 1, 2, 1, 0, 7, 7, 6, 0, 7, 3, 6, 3, 6],
            [4, 2, 4, 1, 4, 0, 6, 6, 7, 0, 2, 6, 6, 6, 6]

        ]
        # 1.4 宝宝初始化
        self.bao = Bao(self.screen, self.sets.baoImages)
        # 获取行列数
        self.row = len(self.sets.floor)
        self.col = len(self.sets.floor[0])
        # 1.5 泡泡存储列表
        self.paos = []
        # 1.6 炸弹存储列表
        self.bombs = []

    '''第二区域： 图形绘制函数'''
    def paint(self):
        # 2.1 绘制地图
        self.paintMap()

        #2.2 绘制建筑物
        self.paintBuild()

        # 2.4 绘制泡泡
        self.paintPao()

        # 2.3 绘制宝宝
        self.paintBao()

        # 2.4 绘制炸弹
        self.paintBomb()

    # 2.1 绘制地板图
    def paintMap(self):
        for i in range(0, self.row):
            for j in range(0, self.col):
                type = self.sets.floor[i][j]
                if type == 1:
                   self.screen.blit(self.sets.diban1,(25+j*50,25+i*50))
                elif type == 2:
                    self.screen.blit(self.sets.diban2, (25+j*50,25+i*50))
                elif type == 3:
                    self.screen.blit(self.sets.diban3, (25+j*50,25+i*50))
                else:
                    self.screen.blit(self.sets.diban4, (25+j*50,25+i*50))

    # 2.2 绘制建筑物
    def paintBuild(self):
        for i in range(0, len(self.build)):
            for j in range(0, len(self.build[0])):
                type = self.build[i][j]
                if type == 0:
                    self.screen.blit(self.sets.shu, (25 + j * 50, 25 + i * 50))
                elif type == 1:
                    self.screen.blit(self.sets.red, (25 + j * 50, 25 + i * 50))
                elif type == 2:
                    self.screen.blit(self.sets.orange, (25 + j * 50, 25 + i * 50))
                elif type == 3:
                    self.screen.blit(self.sets.redHouse, (25 + j * 50, 25 + i * 50))
                elif type == 4:
                    self.screen.blit(self.sets.blueHouse, (25 + j * 50, 25 + i * 50))
                elif type == 5:
                    self.screen.blit(self.sets.yellowHouse, (25 + j * 50, 25 + i * 50))
                elif type == 6:
                    pass
                elif type == 7:
                    self.screen.blit(self.sets.box, (25 + j * 50, 25 + i * 50))

    # 2.3 绘制宝宝
    def paintBao(self):
        self.bao.blitMe()

    # 2.4 绘制泡泡
    def paintPao(self):
        # 迭代所有的泡泡
        for pao in self.paos:
            # 绘制泡泡自己
            pao.blitMe()
    # 2.4 绘制炸弹
    def paintBomb(self):
        # 炸弹迭代
        for bomb in self.bombs:
            bomb.blitMe()

    '''第三区域： 业务逻辑执行区域'''
    def action(self):
        # 3.1 循环迭代事件
        for event in pygame.event.get():
            # 3.2 程序退出
            if event.type == pygame.QUIT:
                sys.exit()
            # 3.3 键盘监听
            if event.type == pygame.KEYDOWN:
                # 3.4 判断键盘字符
                # 上下左右 0,1,2,3
                if event.key == pygame.K_w:
                    # 上
                    self.bao.step(0, self.build)
                elif event.key == pygame.K_s:
                    # 下
                    self.bao.step(1, self.build)
                elif event.key == pygame.K_a:
                    # 左
                    self.bao.step(2, self.build)
                elif event.key == pygame.K_d:
                    # 右
                    self.bao.step(3, self.build)
                # 放炮键
                elif event.key == pygame.K_j and self.bao.number > 0:
                    # 生成并存储
                    pao = Pao(self.screen, self.sets.paoImages, self.bao.x, self.bao.y)
                    self.paos.append(pao)
                    # 更改泡泡数量
                    self.bao.number -= 1

        # 变化业务
        self.change()

    # 3.5 变化业务逻辑执行
    def change(self):
        # 1. 调用泡泡的变化
        # range(len(self.paos))
        for pao in self.paos:
            # 更改图片
            pao.change()
            # 更改生命值
            pao.updateLive()
            # 判断生命值是否结束
            if pao.live < 0:
                # 重点 list列表中迭代删除问题
                # 结束
                self.paos.remove(pao)
                # 爆炸生成
                self.createBomb(pao)
                # 恢复泡泡的数量
                self.bao.number += 1

        # 2.调用炸弹的生命值变化
        for bomb in self.bombs:
            # 更改生命值
            bomb.updateLive()
            # 根据生命值判断是否死亡
            if bomb.live < 0:
                # 删除列表元素
                self.bombs.remove(bomb)
                # 判断该炸弹位置建筑物类型 建筑物销毁
                if self.build[bomb.y][bomb.x] != 6:
                    self.build[bomb.y][bomb.x] = 6
                '''
                道具
                1. 道具类 prop ==> Prop
                # 0 代表泡泡 bao.number
                # 1 代表药水 bao.powr
                self.type = ramdom.randint(0, 1)
                self.image = self.images[self.type]
                2. 随机函数
                if self.judegBuild2(bomb.x, bomb.y)
                    index = random.randint(0, 10)
                    if index == 0:
                        prop = Prop(self.screen, self.)
                        self.props.append(prop)
                3. 绘制函数
                    paintProp()
                def paintProp():
                    for pop in self.props:
                        prop.blitMe()
                4. action ==> 3.4 根据字符判断走位
                    self.bao.step()  ==>
                    self.bao.step(self.props)
                '''
    # 3.5.1 爆炸生成
    def createBomb(self, pao):
        # 1. 中间弹
        centerBomb = Bomb(self.screen, self.sets.bombImages[0], pao.x, pao.y)
        self.bombs.append(centerBomb)
        '''根据泡泡的威力循环迭代添加炸弹'''
        for i in range(0, self.bao.power):
            # 2.上 获取上边的建筑物
            if self.judgeBuild(0, pao.x, pao.y-i) \
                    and pao.UP:
                upBomb = Bomb(self.screen, self.sets.bombImages[0], pao.x, pao.y-(i+1))
                self.bombs.append(upBomb)
            elif self.judgeBuild2(pao.x, pao.y -(i+1)) and pao.UP:
                # 添加炸弹
                upBomb = Bomb(self.screen, self.sets.bombImages[0], pao.x, pao.y - (i + 1))
                self.bombs.append(upBomb)
                # 也做设置
                pao.UP = False
            # 不可炸建筑物
            else:
                pao.UP = False
            # 3.下
            if self.judgeBuild(1, pao.x, pao.y+i) and pao.DOWN:
                downBomb = Bomb(self.screen, self.sets.bombImages[0], pao.x, pao.y+i+1)
                self.bombs.append(downBomb)
            elif self.judgeBuild2(pao.x, pao.y + (i+1)) and pao.DOWN:
                downBomb = Bomb(self.screen, self.sets.bombImages[0], pao.x, pao.y + i + 1)
                self.bombs.append(downBomb)
                pao.DOWN = False
            else:
                pao.DOWN = False
            # 4.左
            if self.judgeBuild(2, pao.x - i, pao.y) and pao.LEFT:
                leftBomb = Bomb(self.screen, self.sets.bombImages[1], pao.x-(i+1), pao.y)
                self.bombs.append(leftBomb)
            elif self.judgeBuild2(pao.x - (i+1), pao.y) and pao.LEFT:
                leftBomb = Bomb(self.screen, self.sets.bombImages[1], pao.x - (i + 1), pao.y)
                self.bombs.append(leftBomb)
                pao.LEFT = False
            else:
                pao.LEFT = False
            # 5.右
            if self.judgeBuild(3, pao.x+i, pao.y) and pao.RIGHT:
                rightBomb = Bomb(self.screen, self.sets.bombImages[1], pao.x+i+1, pao.y)
                self.bombs.append(rightBomb)
            elif self.judgeBuild2(pao.x + (i+1), pao.y) and pao.RIGHT:
                rightBomb = Bomb(self.screen, self.sets.bombImages[1], pao.x + i + 1, pao.y)
                self.bombs.append(rightBomb)
                pao.RIGHT = False
            else:
                pao.RIGHT = False

    # 3.5.1.1 判断建筑物类型
    def judgeBuild(self, dir, paoX, paoY):
        # 根据方向判断类型
        type = 0
        if dir == 0 and 0 <= paoY-1:
            type = self.build[paoY - 1][paoX]
        elif dir == 1 and paoY+1 < 13:
            type = self.build[paoY + 1][paoX]
        elif dir == 2 and 0 <= paoX-1:
            type = self.build[paoY][paoX - 1]
        elif dir == 3 and paoX+1 < 15:
            type = self.build[paoY][paoX + 1]
        # 判断type的值
        return type == 6

    # 3.5.1.2 判断建筑物类型第二版
    def judgeBuild2(self, paoX, paoY):

        # 2. 判断类型及出界
        if 0 <= paoX < 15 \
            and 0<= paoY < 13: \
            # 1.获取建筑物类型
            type = self.build[paoY][paoX]
            return type == 1 or type == 2 or type == 7
        else:
            return False

    '''第四区域： 窗口设置区域'''
    def main(self):
        # 设置标题
        pygame.display.set_caption("泡泡堂")
        # 设置循环
        while True:
            # 绘制窗口和背景图片
            self.screen.blit(self.sets.background,(0, 0))
            # 调用业务执行函数
            self.action()
            # 调用图形绘制函数
            self.paint()
            # 刷新屏幕
            pygame.display.update()

if __name__ == '__main__':
    ppt = PPTGame()
    ppt.main()