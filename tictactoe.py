"""
Tic Tac Toe Player
"""

import math

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
    for i in board:
        for j in i:
            if j == X:
                countX += 1
            elif j == O:
                countO += 1
    if (countX < countO):
        return X
    elif countX > countO:
        return O
    else:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleCoordinates = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleCoordinates.append([i,j])

    return possibleCoordinates

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    action = list(action)
    board[action[0]][action[1]] = player(board)
    return board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    res = utility(board)
    if res == 1:
        return X
    elif res == -1:
        return O
    else:
        return EMPTY

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    status = utility(board)
    if status != 0:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False

    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    for j in range(3):
        row_equal = len({ i for i in board[j]}) == 1 
        if (EMPTY not in board[j]):
            if row_equal and board[j][1] == X:
                return 1
            elif row_equal and board[j][1] == O:
                return -1

    for j in range(3):
        column_equal = len({row[j] for row in board}) == 1 
        if (EMPTY not in board[j]):
            if column_equal and board[j][1] == X:
                return 1
            elif column_equal and board[j][1] == O:
                return -1

    diagTopLeftToRight = len({board[p][p] for p in range(3)}) == 1 
    if diagTopLeftToRight and board[1][1] == X:
        return 1
    elif diagTopLeftToRight and board[1][1] == O:
        return -1

    diagBottomLeftToRight = len({board[-p-1][p] for p in range(3)}) == 1 
    if diagBottomLeftToRight and board[1][1] == X:
        return 1
    elif diagBottomLeftToRight and board[1][1] == O:
        return -1

    return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    
    return action

    raise NotImplementedError

def minValue(board):

    if terminal(board):
        return utility(board)

    v = math.inf
    bestMove = None

    for action in actions(board):
        a, k = maxValue(result(board,action))
        vNew = min(v,k)
        if (vNew < v):
            bestMove = action
            v = vNew

    return bestMove , v

def maxValue(board):

    if terminal(board):
        return utility(board)

    v = -math.inf
    bestMove = None

    for action in actions(board):
        a, k = minValue(result(board,action))
        vNew = max(v,k)
        if (vNew > v):
            bestMove = action
            v = vNew

    return bestMove, v
