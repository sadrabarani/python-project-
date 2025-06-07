import random
from abc import ABC, abstractmethod
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                box = int(input(f"Player {self.symbol}, choose a position (1-9): "))
                board.fill_board(box, self.symbol)
                break
            except Exception as e:
                print(f"Invalid move: {e}. Try again.")


import random

class BotPlayer(Player):
    def __init__(self, symbol, difficulty="hard"):
        super().__init__(symbol)
        self.difficulty = difficulty.lower()

    def make_move(self, board):
        if self.difficulty == "easy":
            self.random_move(board)
        elif self.difficulty == "medium":
            if random.random() < 0.5:
                self.best_move(board)
            else:
                self.random_move(board)
        else:
            self.best_move(board)

    def random_move(self, board):
        """Chooses a random available move."""
        available_moves = [i for i in range(1, 10) if board.is_box_empty(i)]
        move = random.choice(available_moves)
        board.fill_board(move, self.symbol)
        print(f"Bot ({self.symbol}) played randomly at position {move}")

    def best_move(self, board):
        best_score = float('-inf')
        best_move = None

        for i in range(1, 10):
            if board.is_box_empty(i):
                board.fill_board(i, self.symbol)
                score = self.minimax(board, False)
                board.boardGame[i - 1] = " "

                if score > best_score:
                    best_score = score
                    best_move = i

        board.fill_board(best_move, self.symbol)
        print(f"Bot ({self.symbol}) played strategically at position {best_move}")

    def minimax(self, board, is_maximizing):
        winner = board.is_winner()
        if winner == "O": return 1
        if winner == "X": return -1
        if board.is_draw(): return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(1, 10):
                if board.is_box_empty(i):
                    board.fill_board(i, "O")
                    score = self.minimax(board, False)
                    board.boardGame[i - 1] = " "
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(1, 10):
                if board.is_box_empty(i):
                    board.fill_board(i, "X")
                    score = self.minimax(board, True)
                    board.boardGame[i - 1] = " "
                    best_score = min(best_score, score)
            return best_score


class Board:
    def __init__(self):
        self.boardGame = [" "] * 9

    def print_board(self):
        for i in range(9):
            print(self.boardGame[i], end=" | " if i % 3 != 2 else "\n---------\n" if i != 8 else "\n\n")

    def is_full(self):
        return all(cell != " " for cell in self.boardGame)

    def is_winner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for a, b, c in winning_positions:
            if self.boardGame[a] == self.boardGame[b] == self.boardGame[c] and self.boardGame[a] != " ":
                return self.boardGame[a]

        return None

    def is_draw(self):
        return self.is_full() and self.is_winner() is None

    def is_box_empty(self, number):
        return self.is_box_valid(number) and self.boardGame[number - 1] == " "

    def is_box_valid(self, number):
        return 1 <= number <= 9

    def fill_board(self, number, symbol):
        if self.is_box_empty(number):
            self.boardGame[number - 1] = symbol
        else:
            raise Exception("Box is full")

class TicTacToe:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_turn(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        print("""Tic-Tac-Toe Game
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
""")
        while True:
            self.board.print_board()
            self.current_player.make_move(self.board)

            if self.board.is_winner():
                self.board.print_board()
                print(f"The winner is {self.current_player.symbol}!\n")
                break

            if self.board.is_draw():
                self.board.print_board()
                print("It's a draw!\n")
                break

            self.switch_turn()

        print("Game Over!")


def main():
    board = Board()
    mode = input("Choose mode: 1) Human vs Bot  2) Human vs Human\n")

    player1 = HumanPlayer("X")

    if mode == "1":
        difficulty = input("Select difficulty: easy, medium, hard\n").strip().lower()
        player2 = BotPlayer("O", difficulty)
    else:
        player2 = HumanPlayer("O")

    game = TicTacToe(board, player1, player2)
    game.play()


if __name__ == "__main__":
    main()
