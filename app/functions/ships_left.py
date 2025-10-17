def ships_left(board):
    for row in board:
        if "🚢" in row:
            return True
    return False