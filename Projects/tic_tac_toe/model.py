from typing import List
from rich.text import Text
from rich.prompt import Prompt
from utils import console


class Players:
    """Represents the players in a game."""

    def __init__(self, num_players: int = 2):
        """
        Initializes a new instance of the Players class.

        Args:
            num_players (int): The number of players in the game.
        """
        self.num_players = num_players
        self.player_names: List[str] = []
        self.player_colors: List[str] = []
        self.player_marks: List[str] = []
        self.mark_colors: List[str] = []
        self.player_scores: List[int] = []


class Game:
    """Represents a game of Tic Tac Toe."""

    def __init__(self):
        """
        Initializes a new instance of the Game class.

        Initializes an empty 3x3 board with each cell containing a list of a blank space and the color green.
        """
        self.board: List[List[List[str]]] = [
            [[" ", "green"] for _ in range(3)] for _ in range(3)
        ]

    def player_move(
        self, player_name: str, player_color: str, player_mark: str, mark_color: str
    ) -> List[List[str]]:
        """
        Handles a player's move in the game.

        Displays the current player's name and mark color, prompts the player to enter a row and column for their move,
        checks if the chosen position is available, updates the board if it is, and returns the updated board.

        Args:
            player_name (str): The name of the player who is making the move.
            player_color (str): The color of the player's name (e.g. "red", "blue").
            player_mark (str): The symbol that the player is using for their moves (e.g. "X", "O").
            mark_color (str): The color of the player's symbol (e.g. "green", "yellow").

        Returns:
            List of lists representing the updated game board after the player's move.
        """
        console.print(
            Text(f"{player_name}'s Move -", style=f"bold {player_color} blink"),
            Text(player_mark, style=f"bold {mark_color} blink"),
        )
        while True:
            row = (
                int(
                    Prompt.ask(
                        Text("Enter row number", style="green"), choices=["1", "2", "3"]
                    )
                )
                - 1
            )
            col = (
                int(
                    Prompt.ask(
                        Text("Enter column number", style="green"),
                        choices=["1", "2", "3"],
                    )
                )
                - 1
            )
            if self.board[row][col][0] != " ":
                console.print(
                    "That position is already occupied. Please choose a different position.",
                    style="red",
                )
                continue
            self.board[row][col] = [player_mark, mark_color]
            return self.board

    def check_win(self, player_mark: str) -> bool:
        """
        Check if the specified player has won the game.

        Args:
            player_mark (str): The mark assigned to the player being checked.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        # Check rows
        for row in range(3):
            if all(self.board[row][col][0] == player_mark for col in range(3)):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col][0] == player_mark for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i][0] == player_mark for i in range(3)):
            return True
        if all(self.board[i][2 - i][0] == player_mark for i in range(3)):
            return True

        return False


def check_tie(self) -> bool:
    """
    Check if the game has ended in a tie.

    Returns:
        bool: True if the game has ended in a tie, False otherwise.
    """
    for row in range(3):
        for col in range(3):
            if self.board[row][col][0] == " ":
                return False

    return True
