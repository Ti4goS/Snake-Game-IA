import math

X = 0
Y = 1

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
    y_axis_delta = math.pow(coordinates[Y], food[Y])

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


def run_a_star(snake_head):
    return [-20.0,0] #Left