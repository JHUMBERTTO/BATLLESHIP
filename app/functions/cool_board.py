
def cool_board(matrix):
    size = len(matrix)

    # column
    header = "   " + " ".join(f"{i:2}" for i in range(size))
    print(header)

    # row
    for idx, row in enumerate(matrix):
        row_str = " ".join(f"{cell:2}" for cell in row)
        print(f"{idx:2} {row_str}")
