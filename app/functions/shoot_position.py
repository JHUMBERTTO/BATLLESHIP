
def shoot_position(board, coords):
    # Check if the shot is a hit or a miss
        row = int(coords[0])
        column = int(coords[1])
        n = len(board)

        if board[row][column] == "🚢":
            board[row][column] = "~~"
            print("💥 Hit!")
            return board
        else:
            print("❌ Miss!")
            return board

