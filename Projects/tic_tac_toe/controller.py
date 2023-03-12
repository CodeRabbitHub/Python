import random, time
from rich.text import Text
from rich.prompt import Prompt
from utils import console, GameTools
from model import Players, Game
from view import GameDisplay
import subprocess, sys


class PlayerManager:
    """
    Manages the players of the Tic Tac Toe game.

    Args:
        players_instance (Players): The instance of the Players class.

    Attributes:
        players (Players): The instance of the Players class.

    Methods:
        get_player_names: Prompts the user to enter the names of the two players.
        get_player_colors: Generates colors for the two players.
        greet_players: Greets the two players and displays their names and colors.
        shuffle_players: Shuffles the order of the players and their colors.
        get_mark_colors: Generates colors for the X and O marks.
        get_player_marks: Prompts the user to choose their mark (X or O) and displays it.
        initialize_player_scores: Initializes the scores of the two players to 0.
    """

    def __init__(self, players_instance: Players) -> None:
        self.players = players_instance

    def get_player_names(self) -> None:
        """Prompts the user to enter the names of the two players."""
        while True:
            player1 = Prompt.ask(
                Text("Please enter first player name", style="green"), default="Player1"
            ).upper()
            player2 = Prompt.ask(
                Text("Please enter second player name", style="green"),
                default="Player2",
            ).upper()

            if not player1.isalnum() or not player2.isalnum():
                console.print(
                    "Player names can contain only alpha numeric characters",
                    style="red",
                )

            elif player1 == player2:
                console.print(
                    "Both players cannot have same names, please enter the names again",
                    style="red",
                )

            else:
                self.players.player_names = [player1, player2]
                break

    def get_player_colors(self) -> None:
        """Generates colors for the two players."""
        player_colors = GameTools.generate_colors()
        for player in self.players.player_names:
            self.players.player_colors[player] = player_colors.pop()

    def greet_players(self) -> None:
        """Greets the two players and displays their names and colors."""
        player1, player2 = self.players.player_names
        console.print(
            Text("WELCOME", style="bold green"),
            Text(player1, style=f"bold {self.players.player_colors[player1]}"),
            Text("AND", style="green"),
            Text(player2, style=f"bold {self.players.player_colors[player2]}"),
            Text("Let the game begin!", style="green"),
        )

    def shuffle_players(self) -> None:
        """Shuffles the order of the players and their colors."""
        GameTools.animate_shuffle()
        random.shuffle(self.players.player_names)

    def get_player_marks(self) -> None:
        """Prompts the user to choose their mark (X or O) and displays it."""
        player1, player2 = self.players.player_names
        marks = ["X", "O"]
        console.print("\nChoose your mark", style="bold green underline")
        choice = Prompt.ask(
            Text(player1, style=self.players.player_colors[player1]),
            choices=["x", "o"],
            default="x",
            show_default=False,
        ).upper()

        self.players.player_marks[player1] = choice
        marks.remove(choice)
        self.players.player_marks[player2] = marks.pop()

        console.print(
            Text(player1, style=self.players.player_colors[player1]),
            Text(
                f"- {self.players.player_marks[player1]}",
                style=f"{self.players.player_colors[player1]}",
            ),
            Text(player2, style=self.players.player_colors[player2]),
            Text(
                f"- {self.players.player_marks[player2]}",
                style=f"{self.players.player_colors[player2]}",
            ),
        )
        console.print("Starting game..", style="green")

        time.sleep(3)

    def initialize_player_scores(self) -> None:
        """Initializes the scores of the two players to 0."""
        for player in self.players.player_names:
            self.players.player_scores[player] = 0


class GameManager:
    """
    Manages the game flow and tracks scores.

    Args:
        game_display_instance (GameDisplay): An instance of the `GameDisplay` class.

    Attributes:
        game_display (GameDisplay): An instance of the `GameDisplay` class.

    Methods:
        game_loop(round): Manages the game flow for a single round.
        game_over(): Prompts the user to play another round or quit the game.
    """

    def __init__(self, game_display_instance: GameDisplay) -> None:
        """
        Initializes the GameManager instance.

        Args:
            game_display_instance (GameDisplay): An instance of the `GameDisplay` class.
        """
        self.game_display = game_display_instance

    def game_loop(self, round) -> None:
        """
        Manages the game flow for a single round.

        Displays the current board, lets each player make a move in turn, checks for a win or tie, and returns the
        scores for the round.

        Args:
            round (int): The number of the current round.

        Returns:
            list: A list of the current scores for each player.
        """

        self.game_display.display_board(round)
        # current player variable is set to 0
        current_player = 0
        while True:
            # calls the player_move function to let the current player make a move
            player_name = self.game_display.players.player_names[current_player]
            player_color = self.game_display.players.player_colors[player_name]
            player_mark = self.game_display.players.player_marks[player_name]
            self.game_display.game.board = self.game_display.game.player_move(
                player_name, player_color, player_mark
            )
            # displays the updated board after move
            self.game_display.display_board(round)
            # checks if the current player has won
            if self.game_display.game.check_win(player_mark):
                console.print(
                    Text("Congratulations", style="green"),
                    Text(player_name, style=player_color),
                    Text("you have won the game!", style="green"),
                )
                # increase the current player's score
                self.game_display.players.player_scores[player_name] += 1
                return self.game_display.players.player_scores
            # checks if the game is a tie
            if self.game_display.game.check_tie():
                console.print("The game is a tie!", style="green")
                return self.game_display.players.player_scores
            # changes the current player to the next player
            current_player = (current_player + 1) % 2

    def game_over(self) -> bool:
        """
        Prompts the user to play another round or quit the game.

        Returns:
            bool: `True` if the user wants to play another round, `False` otherwise.
        """
        choice = Prompt.ask(
            Text("Do you want to play another round?", style="green"),
            choices=["yes", "no"],
        )
        if choice == "yes":
            return True
        else:
            return False


class GameOptionManager:
    """
    A class to manage game options such as starting, restarting, and exiting the game.

    Attributes:
    -----------
    player_manager_instance: PlayerManager
        An instance of the PlayerManager class.

    Methods:
    --------
    start_game() -> List[str]:
        Prompts the user to start the game and shuffles the players if they agree.
        Returns a list of player names in a random order.
    exit_game() -> bool:
        Prompts the user if they want to exit the game and quits if they agree.
        Returns True if the user agrees to exit, False otherwise.
    restart_game() -> None:
        Clears the console screen, displays a message and waits for 3 seconds before restarting the game.
    """

    def __init__(self, player_manager_instance: PlayerManager) -> None:
        """
        Initializes a new instance of the GameOptionManager class.

        Parameters:
        -----------
        game_instance: Game
            An instance of the Game class.
        player_instance: Players
            An instance of the Players class.
        player_manager_instance: PlayerManager
            An instance of the PlayerManager class.
        """
        self.player_manager = player_manager_instance

    def start_game(self) -> None:
        """
        Prompts the user to start the game and shuffles the players if they agree.

        Returns:
        --------
        List[str]:
            A list of player names in a random order.
        """
        while True:
            game_start_response = Prompt.ask(
                Text("Ready to start the game?", style="green"),
                default="yes",
                choices=["yes", "no"],
                show_default=False,
            )
            if game_start_response == "yes":
                return self.player_manager.shuffle_players()
            elif game_start_response == "no":
                if self.exit_game():
                    quit()
                else:
                    continue

    def exit_game(self) -> bool:
        """
        Prompts the user if they want to exit the game and quits if they agree.

        Returns:
        --------
        bool:
            True if the user agrees to exit, False otherwise.
        """
        exit_game = str(
            Prompt.ask(
                Text("Do you want to exit?", style="green"), choices=["yes", "no"]
            )
        )
        # If the player chooses 'yes', the function prints a farewell message and returns True
        if exit_game == "yes":
            console.print(
                "Thanks for playing! We hope you had a blast. See you next time for more fun and excitement!",
                style="italic rgb(255,255,0)",
            )
            return True
        # If the player chooses 'no', the function returns False
        else:
            return False

    def restart_game(self) -> None:
        """
        Clears the console screen, displays a message and waits for 3 seconds before restarting the game.
        """
        subprocess.run(["cls" if sys.platform == "win32" else "clear"], shell=True)
        console.print("Restarting Game..")
        time.sleep(3)
