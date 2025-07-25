"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in board:
        for cell in row:
            if cell == "X":
                countX += 1
            if cell == "O":
                countO += 1

    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                action = (row, col)
                possible_actions.add(action)

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Not a valid action")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    current_player = None

    # Check rows
    for i in range(3):
        current_player = board[i][0]
        if current_player == board[i][1] and current_player == board[i][2]:
            return current_player

    # Check columns
    for i in range(3):
        current_player = board[0][i]
        if current_player == board[1][i] and current_player == board[2][i]:
            return current_player
        
    # Check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if len(actions(board)) == 0:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def min_value(board):
    if terminal(board):
        return (None, utility(board))
    else:
        v = math.inf
        values = []
        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)
            move = (action, value[1])
            values.append(move)

        for action, value in values:
            v = min(v, value)

        for action, value in values:
            if value == v:
                return (action, value)


def max_value(board):
    if terminal(board):
        return (None, utility(board))
    else:
        v = -math.inf
        values = []
        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)
            move = (action, value[1])
            values.append(move)
        for action, value in values:
            v = max(v, value)

        for action, value in values:
            if value == v:
                return (action, value)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == "X":
        return max_value(board)[0]
    else:
        return min_value(board)[0]


