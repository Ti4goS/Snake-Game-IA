import math

X = 0
Y = 1
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400

def top_left_corner(coordinates):
    return True if coordinates[X]==0.0 and coordinates[Y]==0.0 else False

def top_right_corner(coordinates):
    return True if coordinates[X]==580.0 and coordinates[Y]==0.0 else False

def bottom_left_corner(coordinates):
    return True if coordinates[X]==0.0 and coordinates[Y]==380.0 else False

def bottom_right_corner(coordinates):
    return True if coordinates[X]==580.0 and coordinates[Y]==380.0 else False


def heuristic_g(coordinates, food):
    x_axis_delta = math.pow(coordinates[X] - food[X], 2)
    y_axis_delta = math.pow(coordinates[Y] - food[Y], 2)

    function_h = math.sqrt(x_axis_delta + y_axis_delta)

    return function_h + 1


def define_sucessors(snake_head):
    if top_left_corner(snake_head):
        return [
            [0,20], #Down
            [20,0]  #Right
        ]
    
    if top_right_corner(snake_head):
        return [
            [0,20], #Down
            [-20,0] #Left
        ]

    if bottom_left_corner(snake_head):
        return [
            [0,-20], #Up
            [20,0]  #Right
        ]
    
    if bottom_right_corner(snake_head):
        return [
            [0,-20], #Up
            [-20,0] #Left
        ]

    return [
        [0,-20], #Up
        [0,20], #Down
        [-20,0], #Left
        [20,0]  #Right
    ]


def is_not_in_the_board(coordinates):
    return True if coordinates[X] < 0 or coordinates[X] >= DISPLAY_WIDTH or coordinates[Y] < 0 or coordinates[Y] >= DISPLAY_HEIGHT else False


def is_in_snake_body(coordinates,snake_body):
    try:
        snake_body.index(coordinates)
        return True
    except:
        return False

def define_sucessors_position(snake_head,sucessors):
    return [[snake_head[X]+suc[X],snake_head[Y]+suc[Y]] for suc in sucessors]


def run_a_star(snake_head,snake_body,food_coordinates):
    sucessors = define_sucessors(snake_head)

    sucessors_position = define_sucessors_position(snake_head,sucessors)

    index_best_position = 0
    lowest_cost = 1000.0

    for sucessor_index in range(len(sucessors_position)):
        if is_not_in_the_board(sucessors_position[sucessor_index]):
            continue
        
        if is_in_snake_body(sucessors_position[sucessor_index],snake_body):
            continue
        
        sucessor_cost = heuristic_g(sucessors_position[sucessor_index],food_coordinates)

        if sucessor_cost < lowest_cost:
            lowest_cost = sucessor_cost
            index_best_position = sucessor_index
    
    return sucessors[index_best_position]


print(define_sucessors_position([300.0,300.0],[
        [0,-20], #Up
        [0,20], #Down
        [-20,0], #Left
        [20,0]  #Right
    ]))