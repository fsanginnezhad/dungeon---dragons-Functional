from game.helper.const import CELLS
from game.utils.funcs import (
    draw_map,
    move_player,
    clear_screen,
    get_locations,
    get_valid_moves,
)


def play_game():
    player, dragon, door = get_locations(CELLS)

    while True:
        clear_screen()
        print(f"You are in room {player}")
        valid_moves = get_valid_moves(player)
        print(f"Valid moves are {', '.join(valid_moves)}")
        draw_map(player)
        move = input('Enter your move: ').casefold()
        if move in valid_moves:
            player = move_player(player, move)
            if player == door:
                print('You have escaped!')
                break
            elif player == dragon:
                print('You got eaten by a dragon!')
                break
        else:
            print('Please enter a valid move.')
