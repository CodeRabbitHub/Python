from utils import console
from rich.markdown import Markdown
from rich.text import Text
import subprocess, sys
from model import Game, Players


class IntroDisplay:
    """
    Class for displaying the game introduction and rules.

    Attributes:
        banner (rich.markdown.Markdown): A markdown object containing the game banner.
        rule_title (rich.text.Text): A text object containing the title of the game rules section.
        rules (list): A list of strings containing the game rules.
    """

    def __init__(self) -> None:
        """
        Initialize a GameDisplay object.

        Attributes:
            banner (Markdown): A banner containing the name of the game and the development team.
            rule_title (Text): The title of the game rules section.
            rules (List[str]): A list of game rules.

        Returns:
            None
        """
        self.banner = Markdown(
            """
            ```
              ________________            _________   ______            __________  ______
             /_  __/  _/ ____/           /_  __/   | / ____/           /_  __/ __ \/ ____/
              / /  / // /      ______     / / / /| |/ /      ______     / / / / / / __/   
             / / _/ // /___   /_____/    / / / ___ / /___   /_____/    / / / /_/ / /___   
            /_/ /___/\____/             /_/ /_/  |_\____/             /_/  \____/_____/   
                                                                                    
            ```
            Developed by Team ENIGMA
            """
        )

        self.rule_title = Text(
            " RULES OF THE GAME ", style="bold bright_red on bright_yellow"
        )
        self.rules = [
            "  + The starting player is chosen at random through a shuffle.",
            "  + The player can select their mark from the options of 'X' or 'O'.",
            "  + Each player will take turns to mark their position on the board.",
            "  + The winner is the first player to get three of their marks in a row, in any direction on the board.",
            "  + The game ends when all 9 squares on the board have been filled. If neither player has 3 marks in a row, the game results in a tie.",
        ]

    def show_game_intro(self) -> None:
        """
        Displays the game banner and a message indicating the start of the game.

        Parameters:
        None.

        Returns:
        None.
        """
        console.print(self.banner, style="bold rgb(255,0,0) blink")
        console.print("\n")
        console.print("Let the Fun begins. :alien:", style="rgb(0,255,0)")
        console.print("\n")

    def explain_game_rules(self) -> None:
        """
        Displays the game rules section with a title and a list of rules.

        Parameters:
        None.

        Returns:
        None.
        """
        console.rule(self.rule_title, style="bright_yellow")
        console.print("\n")
        for rule in self.rules:
            console.print(rule, style="green")
        console.print("\n")


class GameDisplay:
    """
    A class for displaying the Tic Tac Toe game board.

    This class is responsible for displaying the current state of the Tic Tac Toe game board on the console.

    Parameters:
    - game_instance (Game): An instance of the `Game` class that represents the current state of the game.
    - players_instance (Players): An instance of the `Players` class that represents the current players in the game.

    Attributes:
    - board (List[List[List[str, str]]]): The game board as a list of rows, where each row is a list of list
      representing the elements in that row. Each list contains a string representing the value of the element,
      and a string representing the color of the element.

    Methods:
    - display_board(round: int) -> None: Displays the current state of the game board on the console for the given
      round.
    """

    def __init__(self, game_instance: Game, players_instance: Players) -> None:
        """
        Initialize a new `GameDisplay` instance with the given game and players instances.

        Parameters:
        - game_instance (Game): An instance of the `Game` class that represents the current state of the game.
        - players_instance (Players): An instance of the `Players` class that represents the current players in the game.
        """
        self.game = game_instance
        self.players = players_instance

    def display_board(self, round: int) -> None:
        """
        Display the current state of the game board.

        The method loops through the rows and elements in the board and uses the `console.print` function to
        display each element with the appropriate formatting. If the current element is the first in the row,
        it will add a leading space before it. If the current element is the last in the row, it will add a
        trailing space after it. It also adds a "|" separator between the element if it is not the last element
        in the row, and also add a '---+---+---' separator if the current row is not the last row.

        Parameters:
        - round (int): The current round of the game.

        Returns:
        None.
        """
        # Clear the console
        subprocess.run(["cls" if sys.platform == "win32" else "clear"], shell=True)
        # Print the round number in bold yellow underline
        console.print(f"GAME ROUND {round}\n", style="bold rgb(255,132,0) underline")
        # Loop through the rows of the board
        for i in range(3):
            # Loop through the columns of the board
            for j in range(3):
                if j == 0:
                    # for the first element in the row, print a leading space
                    console.print(
                        f" {self.game.board[i][j][0]}",
                        style=f"bold {self.game.board[i][j][1]}",
                        end=" ",
                    )
                elif j == 2:
                    # for the last element in the row, print a trailing space
                    console.print(
                        f"{self.game.board[i][j][0]} ",
                        style=f"bold {self.game.board[i][j][1]}",
                    )
                else:
                    console.print(
                        f"{self.game.board[i][j][0]}",
                        style=f"bold {self.game.board[i][j][1]}",
                        end=" ",
                    )
                # If the current column is not the last, print the column seperator
                if j != 2:
                    console.print("|", style="green", end=" ")
            # If the current row is not the last, print the row separator
            if i != 2:
                console.print("---+---+---", style="green")
        # Print a newline at the end
        console.print("\n")

    def display_scores(self) -> None:
        """
        Print the scores of the two players in a console-friendly format.

        Parameters:
        None.

        Returns:
        None.
        """
        player1, player2 = self.players.player_names
        console.print(
            Text("SCORES:", style="green"),
            Text(
                f"{player1}-{self.players.player_scores[player1]}",
                style=self.players.player_colors[player1],
            ),
            Text("AND", style="green"),
            Text(
                f"{player2}-{self.players.player_scores[player2]}",
                style=self.players.player_colors[player2],
            ),
        )
