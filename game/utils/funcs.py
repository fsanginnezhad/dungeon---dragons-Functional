import os
import random


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations(coordinations: list) -> list:
    """
    Selects 3 random coordinates from the list of coordinates and returns them. # noqa E501

    Parameters:
    -----------
    coordinations : list
        A list of tuples representing the coordinates of the balls in the game. # noqa E501

    Returns:
    --------
    locations : list
        A list of 3 tuples representing the random locations selected from the input. # noqa E501
    """
    return random.sample(coordinations, 3)


def get_valid_moves(player: tuple) -> list:
    """
    Finds the valid moves for the player based on their current position.

    Parameters:
    -----------
    player : tuple
        A tuple representing the current position of the player.

    Returns:
    --------
    moves : list
        A list of strings representing the valid moves for the player.
    """
    x, y = player
    moves = ['left', 'right', 'up', 'down']
    if x == 0:
        moves.remove('left')
    if y == 0:
        moves.remove('up')
    if y == 3:
        moves.remove('down')
    if x == 3:
        moves.remove('right')
    return moves


def move_player(player: tuple, move: str) -> tuple:
    """
    Moves the player to a new position based on the given move.

    Parameters:
    -----------
    player : tuple
        A tuple representing the current position of the player.
    move : str
        A string representing the move the player wants to make.

    Returns:
    --------
    new_player : tuple
        A tuple representing the new position of the player.
    """
    x, y = player
    if move == 'left':
        x -= 1
    elif move == 'right':
        x += 1
    elif move == 'up':
        y -= 1
    elif move == 'down':
        y += 1
    return x, y


def draw_map(player_position: tuple) -> None:
    """
    Prints the game map based on the current positions of the balls and the player. # noqa E501

    Parameters:
    -----------
    player_position : tuple
        A tuple representing the position of the player.

    Returns:
    --------
    None
    """
    print(' _' * 4)
    for y in range(4):
        for x in range(4):
            if (x, y) == player_position:
                print('|X', end='')
            else:
                print('|_', end='')
        print('|')
