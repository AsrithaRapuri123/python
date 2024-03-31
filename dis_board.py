row = "+-------+-------+-------+" 
column = "|   {}   |   {}   |   {}   | \n|   {}   |   {}   |   {}   |  \n|   {}   |   {}   |   {}   |"

print(row)

def display_board(): 
    numbers = list(range(1, 10))
    print(row)
    for i in range(3):
        print(column.format(*numbers[i*3:i*3+3]))
        print(row)

display_board()