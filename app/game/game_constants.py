import pygame


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class GameConstants(metaclass=Singleton):
    def __init__(self,width,height,weight,fps):
       self.DISPLAY_WIDTH = width 
       self.DISPLAY_HEIGHT = height
       self.SPRITES_WEIGHT = weight
       self.FPS = fps
       self.screen = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
       self.font_style = pygame.font.SysFont("bahnschrift", 25)
       self.score_font = pygame.font.SysFont("comicsansms", 35)
       self.game_clock = pygame.time.Clock()
       pygame.display.set_caption('Snake Game A* - UFS - DSI')
