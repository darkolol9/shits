import random

LIMIT = 20

PLAYER1 = 0
PLAYER2 = 1


game_is_running = True

def alternate_turn(player):
    if player == PLAYER1:
        return PLAYER2
    else:
        return PLAYER1

PLAYER1 = input('player 1 : enter ur name   ')
PLAYER2 = input('player 2 : enter ur name   ')

curr_player = PLAYER1


while game_is_running and LIMIT > 0:
    temp_number = random.randint(1,LIMIT)
    print('its ',curr_player,'s turn')
    choice = int(input('please choose a number....'))
    print('the limit is...',LIMIT)

    if (choice == temp_number):
        game_is_running = False

    
    curr_player = alternate_turn(curr_player)
    LIMIT = LIMIT - 1 
     

print('the winner is ',curr_player,'\n press any key to end...')










