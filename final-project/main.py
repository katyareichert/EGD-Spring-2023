import pygame
import os

from scenes.title_sequence import TitleSequence
from scenes.counter_k import MainCounter
from scenes.food_selection import FoodSelection
from scenes.drink_selection import DrinkSelection

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define movement constants
FPS = 60

# Load in background music
BG_MUSIC = pygame.mixer.music.load(os.path.join('sound', 'main_music.ogg'))

pygame.display.set_caption("Comfort Cafe")

def main():
   
   # Initialize all scenes
    ts = TitleSequence(WIN, WIDTH, HEIGHT, FPS)
    mc = MainCounter(WIN, WIDTH, HEIGHT, FPS)
    ds = DrinkSelection(WIN, WIDTH, HEIGHT, FPS)
    fs = FoodSelection(WIN, WIDTH, HEIGHT, FPS)

    pygame.mixer.music.play(loops=-1)
    run = ts.run_scene()

    while(run):
        mc.run_scene()
        
        drink_selection = ds.run_scene()
        print(str(drink_selection))

        food_selection = fs.run_scene()
        print(str(food_selection))

    pygame.quit()


if __name__ == "__main__":
    main()