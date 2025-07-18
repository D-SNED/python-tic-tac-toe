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
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True

        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' ':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' ':
                return True

        return False

    def valid_input(self, val):
        valid_guesses = [ "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        return True if val in valid_guesses else False


    def player_action(self, board):

        board.print_board(self.board)

        for i in range(1,10):
            print(f"Its {self.current_player}'s turn")
            player_choice = input("Enter a number (1-9) to mark a square: ")


            if self.valid_input(player_choice):
                pos = int(player_choice) - 1
                row = pos // 3
                col = pos % 3
            else:
                print(f"That input is invalid. Please enter a number 1-9.")
                continue


            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player

                if self.check_winner():
                    board.print_board(self.board)
                    print(f"{self.current_player} has won!")
                    break

                elif self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'
            else:
                input("That square is already taken! Press ENTER to go again")

            board.print_board(self.board)

        if not self.check_winner():
            print(f"It's a tie!")

board = Board()
game = TicTacToe()
game.player_action(board)
