

class pvzObject(object):
    def __init__(self,screen,image,x,y):
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
    #图形绘制
    def blitMe(self):
        self.screen.blit(self.image,(self.x*80+130,self.y*100+90))