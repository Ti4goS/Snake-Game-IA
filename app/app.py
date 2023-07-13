import pygame
from arguments import arguments

BLUE=(0,0,255)
RED=(255,0,0)

def init_game():
    # pygame setup
    pygame.init()
    args = arguments(
        screen= pygame.display.set_mode((600, 600)),
        clock= pygame.time.Clock(),
        running= True
    )
    pygame.display.set_caption('Snake - A* - UFS - DSI')

    return args


def run_game(args):
    while args.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                args.running = False
            
        # fill the screen with a color to wipe away anything from last frame
        args.screen.fill("black")
        pygame.display.update()
        
        # RENDER YOUR GAME HERE


        # flip() the display to put your work on screen
        pygame.display.flip()

        args.clock.tick(60)  # limits FPS to 60


def main():
    """
    Função Principal do programa é a partir dela que tudo é iniciado

    o Jogo é dividido em 3 partes:

    1. Inicialização do jogo
    2. A execução do jogo
    3. Finalização do programa
    """
    args = init_game()
    run_game(args)   
    pygame.quit()    




if __name__ == '__main__':
    main()