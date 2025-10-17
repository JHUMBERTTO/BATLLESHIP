from functions import cool_board as ccb
from random import randint

def fill_board(board, quantity):
    print(f"\n⚓ Place your ships (row,col) use numbers 🚢\n")
    placed = 0
    n = len(board)
    while placed < quantity:
        try:
            print(f"Number of ships to place - {quantity-placed}")
            coordinates = input(f"Coordinates (0-{n-1}, 0-{n-1}): ")

            row = int(coordinates.split(",")[0])
            column = int(coordinates.split(",")[1])
        except ValueError:
            print("❌ Please just write numbers.")
            continue

        if not (0 <= row < n and 0 <= column < n):
            print("⚠️ That position doesnt exist.")
            continue

        if board[row][column] == "🚢":
            print("⚠️ Choose other position this place is already.")
            continue
        board[row][column] = "🚢"
        placed += 1
        ccb.cool_board(board)
    return(board)

def fill_computer_board(board, quantity):
    placed = 0
    n = len(board)
    while placed < quantity:
        row = randint(0, n-1)
        column = randint(0, n-1)

        if board[row][column] == "🚢":
            continue
        board[row][column] = "🚢"
        placed += 1
    return(board)


