import pygame
import os

from scenes.title_sequence import TitleSequence
from scenes.counter_k import MainCounter
from scenes.food_selection import FoodSelection
from scenes.drink_selection import DrinkSelection
from scenes.minigame_mug import MinigameMug
from scenes.draw_fill_line import dashed_line

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define movement constants
FPS = 60

# Load in background music
BG_MUSIC = pygame.mixer.music.load(os.path.join('sound', 'main_music.ogg'))

# Define colors
DRINK_COlORS = {
    1: ((91,61,43), (246,233,215)),
    2: ((193,128,87), (246,237,232)),
    3: ((111,179,143), (181,237,180)),
    4: ((75,49,33), (149,91,54)),
    5: ((56,38,27), (91,61,43)),
    6: ((149,91,54), (250,190,168))
}

pygame.display.set_caption("Comfort Cafe")

def main():
   
   # Initialize all scenes
    ts = TitleSequence(WIN, WIDTH, HEIGHT, FPS)
    mc = MainCounter(WIN, WIDTH, HEIGHT, FPS)
    ds = DrinkSelection(WIN, WIDTH, HEIGHT, FPS)
    fs = FoodSelection(WIN, WIDTH, HEIGHT, FPS)
    mm = MinigameMug(WIN, WIDTH, HEIGHT, FPS)

    pygame.mixer.music.play(loops=-1)
    run = ts.run_scene()

    while(run):
        mc.run_scene()

        drink_selection = ds.run_scene()
        print(str(drink_selection))

        if drink_selection >= 4:
            mm.run_scene(DRINK_COlORS[drink_selection])

        food_selection = fs.run_scene()
        print(str(food_selection))

    pygame.quit()


if __name__ == "__main__":
    main()