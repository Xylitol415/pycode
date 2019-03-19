'''
泡泡
'''
from nexonObject import NexonObject

class Pao(NexonObject):
    # 1.初始化
    def __init__(self, screen, images, baoX, baoY):
        self.screen = screen
        # 获取泡泡的图片集
        self.images = images
        # 获取泡泡的图片
        self.image = self.images[0]
        # 获取宝宝的坐标
        self.x = baoX
        self.y = baoY
        # 设置泡泡生命值
        # 时间设置
        self.live = 50
        # 调用父类函数
        super(Pao, self).__init__(screen, self.image, self.x, self.y)
        # 属性
        # 图片集转换值
        self.index = 0
        # 方向值 爆炸物延伸方向
        # 爆炸物遇到不可炸建筑物 停止 True --> False
        self.UP = True
        self.DOWN = True
        self.LEFT = True
        self.RIGHT = True

    # 运动
    def change(self):
        # 1.改变图片集转换值
        self.index += 1
        # 2. 根据图片集转换值修改变量频率
        # index ==> 0/2 = 0 % 2 =  0
        # index ==> 1/2 = 0 % 2 = 0
        # index ==> 2/2 = 1 % 2 = 1
        # index 控制图片频率的
        ix = self.index/10%len(self.images)
        # 根据频率x修改图片 ix 必须为int类型
        self.image = self.images[int(ix)]

    def updateLive(self):
        self.live -= 1
    # 抽象函数
    def outOfBounds(self, dir):
        pass

