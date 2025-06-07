import random

import advance_tic_tac_toe


class TicTacToe:

    def __init__(self, board):
        self.board = board

    def play_bot(self):
        board = self.board
        ran_box = random.randint(1, 9)

        while not board.is_box_empty(ran_box):
            ran_box = random.randint(1, 9)

        self.board.fill_board(ran_box, "O")
        board.printBoard()

        if board.is_winner():
            print(f"The winner is {board.is_winner()}\n")
            return True  # Game over
        if board.is_draw():
            print("It's a draw!\n")
            return True  # Game over

        return False  # Continue playing


class Board:

    def __init__(self):
        self.boardGame = [" "] * 9

    def printBoard(self):
        for i in range(0, 9):
            print(self.boardGame[i], end=" | " if i % 3 != 2 else "\n---------\n" if i != 8 else "\n\n")

    def is_full(self):
        for i in range(0, 9):
            if self.boardGame[i] == " ":
                return False
        return True

    def is_winner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for pos in winning_positions:
            a, b, c = pos
            if self.boardGame[a] == self.boardGame[b] == self.boardGame[c] and self.boardGame[a] != " ":
                return self.boardGame[a]  # Return "X" or "O" (the winner)

        return None  # No winner yet

    def is_draw(self):
        if (self.is_full()):
            if (self.is_winner() != "X" and self.is_winner() != "O"):
                return True
        return False

    def is_box_empty(self, number):
        if self.is_box_valid(number):
            if self.boardGame[number - 1] == " ":
                return True
        else:
            False

    def is_box_valid(self, number):
        if (int)(number) < 1 or (int)(number) > 9:
            return False
        return True

    def fill_board(self, number, letter):
        if self.is_box_empty(number):
            self.boardGame[number - 1] = letter
        else:
            raise Exception("Box is full")


def play():
    board = Board()
    game = TicTacToe(board)
    print("""tic tac toe game
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
""")
    while True:
        choice = input("1.play 2.show board 3.exit 4.advance tic tac toe\n")
        if choice == "1":
            box = (int)(input("ur position 1-9"))
            try:
                board.fill_board(box, "X")
            except(Exception) as e:
                print("the box is full")
                continue
            board.printBoard()
            if board.is_winner() != None:
                print(f"the winner is {board.is_winner()}\n")
                break
            if board.is_draw():
                print(f"draw \n")
                break
            if game.play_bot():
                break
        elif choice == "2":
            board.printBoard()
        elif choice == "3":
            break
        elif choice == "4":
            advance_tic_tac_toe.main()
        else:
            raise Exception("invalid choice")



def main():
    try:
        play()
    except Exception as e:
        print(e.__cause__)
    finally:
        print("good bye")




if __name__ == "__main__":
    main()

