from typing import List, Tuple, Union
import random, sys, colorsys, time
from rich.console import Console

# Initialize a console object
console = Console()


class GameTools:
    @staticmethod
    def generate_colors(number=2) -> List[str]:
        """
        Generates a list of specified number of random colors in RGB format

        Parameters:
        number (int, optional): number of colors to generate, default is 2

        Returns:
        List[str]: List of RGB colors in string format

        Example:
        >>> generate_colors(3)
        ['rgb(200, 130, 120)', 'rgb(50, 60, 70)', 'rgb(10, 20, 30)']
        """
        colors = []
        for _ in range(number):
            h, s, l = (
                random.random(),
                0.5 + random.random() / 2.0,
                0.4 + random.random() / 5.0,
            )
            r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
            colors.append(str(f"rgb({r},{g},{b})"))
        return colors

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
