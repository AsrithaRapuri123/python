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