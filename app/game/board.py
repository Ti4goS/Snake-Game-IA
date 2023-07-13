import random


class Board:
    def __init__(self):
        """
            Quando o Grid está com valor:
              0 - o espaço está livre\n
              1 - O espaço contém uma maça\n
              -1 - O espaço Contem a cabeça da cobra\n
              -2 - O espaço contem o corpo da cobra\n
        """
        self.WIDTH = 640
        self.HEIGHT = 360
        self.WEIGHT = 20
        self.__grid = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #1
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #2
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #3
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #4
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #5
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #6
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #7
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #8
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #9
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #10
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #11
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #12
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #13
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #14
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #15
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #16
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #17
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #18
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #19
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #20
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #21
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #22
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #23
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #24
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #25
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #26
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #27
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #28
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #29
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #30
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #31
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #32
        ]

        self.create_apple()
        self.create_snake()




    def grid(self) -> list[list[int]]:
        return self.__grid
    

    def insert_in_grid(self,x_position,y_position,value):
        self.__grid[x_position][y_position] = value
    

    def create_apple(self):
        """
        Procura um espaço válido para a maça
        """
        x_position = round(random.randrange(0, self.WIDTH - self.WEIGHT) / self.WEIGHT)
        y_position = round(random.randrange(0, self.HEIGHT - self.WEIGHT) / self.WEIGHT)

        if self.__is_not_valid(x_position,y_position):
            self.update_grid()
            return
        
        self.insert_in_grid(x_position,y_position,1)
        return


    def create_snake(self):
        """
        Procura um espaço válido para a maça
        """
        x_position = round(random.randrange(0, self.WIDTH - self.WEIGHT) / self.WEIGHT)
        y_position = round(random.randrange(0, self.HEIGHT - self.WEIGHT) / self.WEIGHT)

        if self.__is_not_valid(x_position,y_position):
            self.update_grid()
            return
        
        self.insert_in_grid(x_position,y_position,-1)
        return
    
            
    def __is_not_valid(self,x_position,y_position):
        """
            Verifica se é uma posição NÃO VÁLIDA no tabuleiro
        """
        if self.__grid[x_position][y_position] != 0:
            return True
        
        return False