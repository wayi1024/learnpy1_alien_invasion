import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings=Settings()

        #初始化屏幕大小和标题
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self)
    
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._upadate_screen()

    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                #注意一个是type，一个是key
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    self.ship.moving_right=False

    def _upadate_screen(self):
        """更新屏幕上的图像并切换到新屏幕"""
        #重绘屏幕、船
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__=="__main__":
    ai=AlienInvasion()
    ai.run_game()

