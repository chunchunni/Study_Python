import pygame
from pygame import rect

class Ship():
    def __init__(self,screen):
        # 初始化飞船及其位置
        self.screen = screen

        # 加载飞船的图像并获取其外接矩形，Python通过利用矩阵来处理图像提高效率
        self.image = pygame.image.load(r'/home/chunchunni/桌面/Study_Python/Alien_Attack/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 新的飞船会被初始化到屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
