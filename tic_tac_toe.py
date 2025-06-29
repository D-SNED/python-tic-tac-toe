class Board:
    def print_board(self,board):
        for i in range(len(board)):
            if i < len(board) - 1:
                print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " ")
                print("-----------------")
            else:
                print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " ")


class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def player_action(self):

        player_choice = input("Enter a number (1-9) to mark a square: ")

        pos = int(player_choice) - 1
        row = pos // 3
        col = pos % 3

        self.board[row][col] = 'X'

game = TicTacToe()
board = Board()

game.player_action()
board.print_board(game.board)
