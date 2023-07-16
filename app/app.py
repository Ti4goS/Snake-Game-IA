
import pygame
import random
import math
from const import Color
from game import GameConstants, Screen, run_a_star

X = 0
Y = 1

pygame.init()

game_info = GameConstants(
    width=600,
    height=400,
    weight=20,
    fps=15
)

screen_resources = Screen(game_info)


def get_random_spot(snake_list):
    foodx = round(random.randrange(0, game_info.DISPLAY_WIDTH -
                  game_info.SPRITES_WEIGHT) / game_info.SPRITES_WEIGHT) * game_info.SPRITES_WEIGHT
    foody = round(random.randrange(0, game_info.DISPLAY_HEIGHT -
                  game_info.SPRITES_WEIGHT) / game_info.SPRITES_WEIGHT) * game_info.SPRITES_WEIGHT
    
    try: 
        snake_list.index([float(foodx), float(foody)])
        return get_random_spot(snake_list)
    
    except:
        return [foodx, foody]
        

    


def singleplayer_commands(event):
    x_axis_change = 0
    y_axis_change = 0

    if event.key == pygame.K_LEFT:
        x_axis_change = -game_info.SPRITES_WEIGHT
        y_axis_change = 0
    elif event.key == pygame.K_RIGHT:
        x_axis_change = game_info.SPRITES_WEIGHT
        y_axis_change = 0
    elif event.key == pygame.K_UP:
        y_axis_change = -game_info.SPRITES_WEIGHT
        x_axis_change = 0
    elif event.key == pygame.K_DOWN:
        y_axis_change = game_info.SPRITES_WEIGHT
        x_axis_change = 0

    return [x_axis_change, y_axis_change]


def is_not_in_the_board(coordinates):
    return True if coordinates[X] < 0 or coordinates[X] >= game_info.DISPLAY_WIDTH or coordinates[Y] < 0 or coordinates[Y] >= game_info.DISPLAY_HEIGHT else False


def snake_eats_food(snake, food):
    return True if snake[X] == food[X] and snake[Y] == food[Y] else False


def update_snake_body(snake_List,length_of_snake):
    if len(snake_List) > length_of_snake:
            snake_List.pop(0)  
    return snake_List


def head_touch_body(snake_list, snake_head):
    for x in snake_list[:-1]:
        if x == snake_head:
            return True
    return False


def update_snake_head(coordinates):
    head = []
    head.append(coordinates[X])
    head.append(coordinates[Y])
    return head


def gameLoop():
    game_over = False
    game_close = False

    snake_coordinates = [game_info.DISPLAY_WIDTH /
                         2, game_info.DISPLAY_HEIGHT / 2]

    changes = [0, 0]

    snake_List = []
    snake_Head = []

    snake_Head.append(snake_coordinates[X])
    snake_Head.append(snake_coordinates[Y])
    length_of_snake = 1

    food_coordinates = get_random_spot(snake_List)

    while not game_over:

        while game_close == True:
            screen_resources.loser_screen(length_of_snake)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                changes = singleplayer_commands(event)

        #changes = run_a_star(snake_Head)
        #print('Snake Head:\n' + str(snake_Head) + '\nSnake List:\n' + str(snake_List))

        snake_coordinates[X] += changes[X]
        snake_coordinates[Y] += changes[Y]

        # Verificar se as coordenadas estão dentro das bordas do jogo
        if is_not_in_the_board(snake_coordinates):
            game_close = True

        #desenha a maça na tela
        game_info.screen.fill(Color.black)
        screen_resources.draw_apple(food_coordinates)

        #adiciona a nova posição da cabeça da cobra no tabuleiro
        snake_Head = update_snake_head(snake_coordinates)
        snake_List.append(snake_Head)

        #atualiza o corpo da cobra para remover a última posição
        snake_List = update_snake_body(snake_List,length_of_snake)

        if head_touch_body(snake_List, snake_Head):
            game_close = True

        #desenha a cobra e o placar na tela
        screen_resources.print_snake_on_screen(snake_List)
        screen_resources.print_score_board(length_of_snake - 1)

        pygame.display.update()

        if snake_eats_food(snake_coordinates, food_coordinates):
            food_coordinates = get_random_spot(snake_List)
            length_of_snake += 1

        game_info.game_clock.tick(15)
    pygame.quit()
    quit()


gameLoop()
