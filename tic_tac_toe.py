class Board:
    def print_board(self, board):
        for i in range(len(board)):
            if i < len(board) - 1:
                print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " ")
                print("-----------------")
            else:
                print(" ", board[i][0], " | ", board[i][1], " | ", board[i][2], " ")


class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = 'X'

    def check_winner(self):
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True

        return False




    def player_action(self, board):

        for i in range(1,10):
            player_choice = input("Enter a number (1-9) to mark a square: ")

            pos = int(player_choice) - 1
            row = pos // 3
            col = pos % 3

            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player

                if self.check_winner():
                    print(f'{self.current_player} has won!')
                elif self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'
            else:
                input("That square is already taken! Press ENTER to go again")

            board.print_board(self.board)

board = Board()
game = TicTacToe()
game.player_action(board)
