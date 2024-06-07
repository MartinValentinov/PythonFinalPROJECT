from constants import *

player_move_left_1 = pygame.image.load('pictures/player_1_3.png')
player_move_left_2 = pygame.image.load('pictures/player_2.png')
player_move_left_3 = pygame.image.load('pictures/player_1_3.png')
player_move_left_4 = pygame.image.load('pictures/player_4.png')

player_move_left = [player_move_left_1, player_move_left_2, player_move_left_3, player_move_left_4]
player_move_left_index = 0
player_move_left_surf = player_move_left[player_move_left_index]

def player_move_left_animations():
    global player_move_left_surf, player_move_left_index

    player_move_left_index += 0.05
    if player_move_left_index >= len(player_move_left):
        player_move_left_index = 0
    player_move_left_surf = player_move_left[int(player_move_left_index)]
    return player_move_left_surf