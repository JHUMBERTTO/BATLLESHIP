

# This function create the matrix/board based on the size u specify
def create_board(size):
    # init array
    try:
        matrix = []

        if size <= 2: raise ValueError("The size must be greater than 2")
        if size <= 2: raise ValueError("The size must be greater than 2")
        if size > 10: raise ValueError("The size must be less than 10")

        if size != int(size): raise ValueError("The size must be an integer")

        for i in range(size):
            # python allows you to multiply the array by an int and then concat
            row = ["~~"] * size
            matrix.append(row)
        return(matrix)
    except ValueError as e:
        print(f"❌ Error: {e}. Try again.")
        