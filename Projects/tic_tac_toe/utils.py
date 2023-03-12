from typing import List, Tuple, Union
import random, sys, colorsys, time
from rich.console import Console

# Initialize a console object
console = Console()


class GameTools:
    @staticmethod
    def generate_colors() -> List[str]:
        """
        Returns a list of `number` random colors in RGB format from an electric neon color palette.

        Args:
            number (int): The number of colors to generate. Default is 2.

        Returns:
            List[str]: A list of `number` colors in RGB format.

        Example:
            >>> GameTools.generate_colors(3)
            ['rgb(255,0,255)', 'rgb(255,255,0)', 'rgb(0,255,0)']
        """
        electric_neon_color_palette = [
            "rgb(255,0,0)",
            "rgb(255,255,0)",
            "rgb(0,255,255)",
            "rgb(255,0,255)",
        ]
        random.shuffle(electric_neon_color_palette)
        return electric_neon_color_palette[:2]

    @staticmethod
    def animate_shuffle(num_of_rolls=2) -> None:
        """
        Animates a shuffle process in the console

        Parameters:
        num_of_rolls (int, optional): number of rolls for the shuffle animation, default is 2

        Returns:
        None
        """
        for i in range(num_of_rolls * 4):
            if i % 4 == 0:
                sys.stdout.write("\rShuffling Players |")
            elif i % 4 == 1:
                sys.stdout.write("\rShuffling Players /")
            elif i % 4 == 2:
                sys.stdout.write("\rShuffling Players -")
            else:
                sys.stdout.write("\rShuffling Players \\")
            sys.stdout.flush()
            time.sleep(0.5)
        sys.stdout.write("\rDone!    ")
        sys.stdout.write("\033[K")
        sys.stdout.write("\n")
        sys.stdout.flush()
