def print_board():
    board = [['X',' ','O'],[' ','X','O'],[' ','O','X']]
    for i in range(len(board)):
        if i < len(board) - 1:
            print(' ', board[i][0], ' | ', board[i][1], ' | ', board[i][2], ' ')
            print('-----------------')
        else:
            print(' ', board[i][0], ' | ', board[i][1], ' | ', board[i][2], ' ')

print_board()
