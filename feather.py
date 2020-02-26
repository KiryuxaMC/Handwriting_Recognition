import pygame
from pygame.sprite import Sprite

class Feather(Sprite):
    '''Класс пера'''
    def __init__(self, screen, sett):
        '''Загрузка изображения'''
        self.screen = screen
        self.settings = sett
        self.image = pygame.image.load('images/feather.png')
        self.rect = self.image.get_rect()
        self.visible = False
    
    def blit_me(self, mouse_x, mouse_y):
        '''Отрисовка метода'''
        self.rect.x = mouse_x
        self.rect.y = mouse_y
        self.screen.blit(self.image, self.rect)