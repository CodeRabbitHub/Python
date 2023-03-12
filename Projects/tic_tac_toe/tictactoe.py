# Import necessary modules and classes
from view import IntroDisplay, GameDisplay
from model import Players, Game
from controller import PlayerManager, GameManager, GameOptionManager
from utils import console
from rich.text import Text

if __name__ == "__main__":
    # Start the game loop
    while True:
        round = 1
        # Display the Game introduction
        intro = IntroDisplay()
        intro.show_game_intro()
        intro.explain_game_rules()
        # Creating and initiliazing players and recording their data
        players = Players()
        player_manager = PlayerManager(players)
        player_manager.get_player_names()
        player_manager.get_player_colors()
        player_manager.greet_players()
        player_manager.initialize_player_scores()
        # Start the game round
        while True:
            # Create game instances and game options
            game = Game()
            game_option = GameOptionManager(player_manager)
            # Start the game
            game_option.start_game()
            # Shuffle players and get their mark colors and marks
            player_manager.get_player_marks()
            # Create game display and game manager instances and start the game loop
            game_display = GameDisplay(game, players)
            game_manager = GameManager(game_display)
            players.player_scores = game_manager.game_loop(round)
            # Display the scores
            game_display.display_scores()
            # Check if the game is over and ask the player for another round
            if game_manager.game_over():
                console.print("Gear up for another round!", style="green")
                round += 1
                continue
            break
        # Check if the player wants to exit or restart the game
        if game_option.exit_game():
            quit()
        else:
            game_option.restart_game()
