import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏
    pygame.init()
    ai_settings = Settings()
    # 实参元组（*，*）用来指定游戏窗口的大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigt))
    # 创建窗口
    pygame.display.set_caption("Alien Invasion")  

    ship = Ship(screen)

    while True:
        for event in pygame.event.get():
            # 单击关闭窗口
            if event.type == pygame.QUIT:
                sys.exit()
        # 更新时会重新绘制屏幕
        screen.fill(ai_settings.bg_color)

        ship.blitme()

        # 更新屏幕，隐藏旧屏幕
        pygame.display.flip()

run_game()
