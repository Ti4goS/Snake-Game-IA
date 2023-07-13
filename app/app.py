import pygame
import random
from arguments import Color
from game import GameConstants

pygame.init()

game_info = GameConstants(
    width= 600,
    height= 400,
    weight= 20,
    fps = 15
)

X = 0
Y = 1

def your_score(score):
    value = game_info.score_font.render("Your Score: " + str(score), True, Color.yellow)
    game_info.screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(game_info.screen, Color.green, [x, y, snake_block, snake_block])


def message(msg, color, x_pos, y_pos):
    mesg = game_info.font_style.render(msg, True, color)
    game_info.screen.blit(mesg, [x_pos, y_pos])


def get_random_spot(grid):
    foodx = round(random.randrange(0, game_info.DISPLAY_WIDTH - game_info.SPRITES_WEIGHT) / game_info.SPRITES_WEIGHT) * game_info.SPRITES_WEIGHT
    foody = round(random.randrange(0, game_info.DISPLAY_HEIGHT - game_info.SPRITES_WEIGHT) / game_info.SPRITES_WEIGHT) * game_info.SPRITES_WEIGHT

    if grid[foodx // game_info.SPRITES_WEIGHT][foody // game_info.SPRITES_WEIGHT] != 0:
        return get_random_spot(grid)
    
    return [foodx,foody]

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
    
    return [x_axis_change,y_axis_change]


def loser_screen(length_of_snake):
    game_info.screen.fill(Color.black)
    message("You Lost! Press C-Play Again or Q-Quit", Color.red, game_info.DISPLAY_WIDTH / 6, game_info.DISPLAY_HEIGHT / 3)
    your_score(length_of_snake - 1)
    pygame.display.update()

def is_not_in_the_board(coordinates):
    return True if coordinates[X] < 0 or coordinates[X] >= game_info.DISPLAY_WIDTH or coordinates[Y] < 0 or coordinates[Y] >= game_info.DISPLAY_HEIGHT  else False


def snake_eats_food(snake,food):
    return True if snake[X] == food[X] and snake[Y] == food[Y] else False


def gameLoop():
    game_over = False
    game_close = False

    snake_coordinates = [game_info.DISPLAY_WIDTH / 2, game_info.DISPLAY_HEIGHT / 2]

    changes = [0,0]

    snake_List = []
    length_of_snake = 1

    # Calcular o tamanho da matriz
    matrix_width = game_info.DISPLAY_WIDTH // game_info.SPRITES_WEIGHT
    matrix_height = game_info.DISPLAY_HEIGHT // game_info.SPRITES_WEIGHT

    # Vetor bidimensional para armazenar as informações da janela
    window_data = [[0] * matrix_height for _ in range(matrix_width)]

    food_coordinates = get_random_spot(window_data)

    while not game_over:

        while game_close == True:
            loser_screen(length_of_snake)

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

        snake_coordinates[X] += changes[X]
        snake_coordinates[Y] += changes[Y]

        game_info.screen.fill(Color.black)
        pygame.draw.rect(game_info.screen, Color.red, [food_coordinates[X], food_coordinates[Y], game_info.SPRITES_WEIGHT, game_info.SPRITES_WEIGHT])
        snake_Head = []
        snake_Head.append(snake_coordinates[X])
        snake_Head.append(snake_coordinates[Y])

        # Verificar se as coordenadas estão dentro das bordas do jogo
        if is_not_in_the_board(snake_coordinates):
            game_close = True

        else:
            snake_List.append(snake_Head)
            # Atualização do vetor bidimensional
            window_data = [[0] * matrix_height for _ in range(matrix_width)]
            # Posição da cabeça da cobra
            window_data[int(snake_coordinates[X] // game_info.SPRITES_WEIGHT)][int(snake_coordinates[Y] // game_info.SPRITES_WEIGHT)] = -1


        if len(snake_List) > length_of_snake:
            tail = snake_List.pop(0)
            # Exclusão da posição antiga da cobra
            if 0 <= int(tail[0] // game_info.SPRITES_WEIGHT) < matrix_width and 0 <= int(tail[1] // game_info.SPRITES_WEIGHT) < matrix_height:
                window_data[int(tail[0] // game_info.SPRITES_WEIGHT)][int(tail[1] // game_info.SPRITES_WEIGHT)] = 0

                    

        for x, y in snake_List[:-1]:
            # Corpo da cobra
            if 0 <= int(x // game_info.SPRITES_WEIGHT) < matrix_width and 0 <= int(y // game_info.SPRITES_WEIGHT) < matrix_height:
                window_data[int(x // game_info.SPRITES_WEIGHT)][int(y // game_info.SPRITES_WEIGHT)] = 1

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(game_info.SPRITES_WEIGHT, snake_List)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if snake_eats_food(snake_coordinates,food_coordinates):
           food_coordinates = get_random_spot(window_data)
           length_of_snake += 1

        game_info.game_clock.tick(game_info.FPS)

    pygame.quit()
    quit()


gameLoop()
