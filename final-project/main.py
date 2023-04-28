# Library Imports
import pygame

import sys
import os

import subprocess
import pkg_resources
from fontTools.ttLib import TTFont

# Check for required packages
required = {'pygame', 'fonttools'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# Scene Imports
from scenes.title_sequence import TitleSequence
from scenes.options_page import OptionsPage
from scenes.counter_k import MainCounter
from scenes.food_selection import FoodSelection
from scenes.drink_selection import DrinkSelection
from scenes.minigame_mug import MinigameMug
from scenes.minigame_tumblr import MinigameTumblr

# Initialize pygame packages
pygame.font.init()
# font = TTFont(os.path.join('dialogue/font.ttf', 'PixeloidSans-JR6qo.ttf'))
# font.save('dialogue')
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define movement constants
FPS = 60

# Load in background music
BG_MUSIC = pygame.mixer.music.load(os.path.join('sound', 'main_music.ogg'))

# Load in fonts
font_big = pygame.font.SysFont('pixeloidsansjr6qo', 30)
font_small = pygame.font.SysFont('pixeloidsansjr6qo', 18)

# Define colors
DRINK_COlORS = {
    1: ((91,61,43), (246,233,215)),
    2: ((193,128,87), (246,237,232)),
    3: ((111,179,143), (181,237,180)),
    4: ((75,49,33), (149,91,54)),
    5: ((56,38,27), (91,61,43)),
    6: ((149,91,54), (250,190,168))
}

# Set Window Caption
pygame.display.set_caption("Comfort Cafe")

def main():
   
    # Initialize options page
    op = OptionsPage(WIN, WIDTH, HEIGHT, FPS, pygame.mixer.music.get_volume(), font_big, font_small)

    # Initialize all scenes
    ts = TitleSequence(WIN, WIDTH, HEIGHT, FPS, op)
    mc = MainCounter(WIN, WIDTH, HEIGHT, FPS)
    ds = DrinkSelection(WIN, WIDTH, HEIGHT, FPS)
    fs = FoodSelection(WIN, WIDTH, HEIGHT, FPS)
    mm = MinigameMug(WIN, WIDTH, HEIGHT, FPS)
    mt = MinigameTumblr(WIN, WIDTH, HEIGHT, FPS)

    pygame.mixer.music.play(loops=-1)

    # !!!!!!!!!!!!!!!! CHANGE THIS !!!!!!!!!!!!!!!!!!!!!!!!!
    pygame.mixer.music.set_volume(0)  # !!!!!!!!!!!!!!!! CHANGE THIS !!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!! CHANGE THIS !!!!!!!!!!!!!!!!!!!!!!!!!

    run = ts.run_scene()

    while(run):
        mc.run_scene()

        drink_selection = ds.run_scene()
        print(str(drink_selection))

        if drink_selection >= 4:
            mm.run_scene(DRINK_COlORS[drink_selection])
        else:
            mt.run_scene(DRINK_COlORS[drink_selection])

        food_selection = fs.run_scene()
        print(str(food_selection))

    pygame.quit()


if __name__ == "__main__":
    main()