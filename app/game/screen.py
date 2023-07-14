import pygame
from arguments import Color

class Screen:
    def __init__(self,game_info) -> None:
        self.__game_info = game_info
    
    def print_score_board(self,score):
        value = self.__game_info.score_font.render("Your Score: " + str(score), True, Color.yellow)
        self.__game_info.screen.blit(value, [0, 0])

    def print_snake_on_screen(self, snake_list):
        for x, y in snake_list:
            pygame.draw.rect(self.__game_info.screen, Color.green, [x, y, self.__game_info.SPRITES_WEIGHT, self.__game_info.SPRITES_WEIGHT])

    def __message(self,msg, color, x_pos, y_pos):
        mesg = self.__game_info.font_style.render(msg, True, color)
        self.__game_info.screen.blit(mesg, [x_pos, y_pos])

    def loser_screen(self,length_of_snake):
        self.__game_info.screen.fill(Color.black)
        self.__message("You Lost! Press C-Play Again or Q-Quit", Color.red, self.__game_info.DISPLAY_WIDTH / 6, self.__game_info.DISPLAY_HEIGHT / 3)
        self.print_score_board(length_of_snake - 1)
        pygame.display.update()

    def draw_apple(self,food_coordinates):
        pygame.draw.rect(self.__game_info.screen, Color.red, [food_coordinates[0], food_coordinates[1], self.__game_info.SPRITES_WEIGHT, self.__game_info.SPRITES_WEIGHT])
