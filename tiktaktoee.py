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

def make_list_of_free_fields(board):
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["x", "o"]:
                free.append((i, j))
    return free

board = [['', '', ''], ['', 'x', ''], ['', '', '']]  
free_fields = make_list_of_free_fields(board)
print(free_fields)

def enter_move(board):
    ok = False
    while not ok:
        move=input("enter your move:")
        ok=len(move)==1 and move>="1" and move<="9"
        if not ok:
            print("bad input")
            continue
        move=int(move)-1
        row=move//3
        col=move%3
        sign=board[row][col]
        ok=sign not in ["X","O"] 
        if not ok:
            print("It is occupied repeat your input")
            continue
    board[row][col]="O"

