def display_board(board):
    for row in board:
        print("+---------+---------+---------+")
        print("|         |         |         |")
        print("|    {}    |    {}    |    {}    |".format(row[0], row[1], row[2]))
        print("|         |         |         |")
    print("+---------+---------+---------+")

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

display_board(board)