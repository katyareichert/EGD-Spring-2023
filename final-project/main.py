# Library Imports
import sys
import os

# Library Imports
import pygame
from ast import literal_eval
from scenes.get_random_order import get_random_order

# Scene Imports
from scenes.title_sequence import TitleSequence
from scenes.options_page import OptionsPage
from scenes.counter_k import MainCounter
from scenes.counter_dialogue import DialogueCounter
from scenes.food_selection import FoodSelection
from scenes.drink_selection import DrinkSelection
from scenes.minigame_mug import MinigameMug
from scenes.minigame_tumblr import MinigameTumblr
from scenes.end_screen import EndScreen

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
DOOR_SOUND = pygame.mixer.Sound(os.path.join('sound', 'door_chime.mp3'))
DOOR_SOUND.set_volume(0.6)

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
    dc = DialogueCounter(WIN, WIDTH, HEIGHT, FPS)
    ds = DrinkSelection(WIN, WIDTH, HEIGHT, FPS)
    fs = FoodSelection(WIN, WIDTH, HEIGHT, FPS)
    mm = MinigameMug(WIN, WIDTH, HEIGHT, FPS)
    mt = MinigameTumblr(WIN, WIDTH, HEIGHT, FPS)
    es = EndScreen(WIN, WIDTH, HEIGHT, FPS, font_small)

    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(1)

    run = True

    while (run):
        # Run title sequence
        char, vol = ts.run_scene()
        if vol > 0.1:
            DOOR_SOUND.set_volume(vol-0.05)
        else:
            DOOR_SOUND.set_volume(0)

        # Get scene order
        scene_order = get_random_order()

        # Main game loop
        for scene_file in scene_order:

            # Read dialogue file
            with open(scene_file) as fp:
                file_lines = fp.readlines()

            # Signal new customer
            DOOR_SOUND.play()
            mc.run_scene(char)
            
            # For line in file
            for i in range(len(file_lines)):

                # If blank line, empty scene
                if file_lines[i] == '\n':
                    mc.run_scene(char)

                # If lines of dialogue
                elif file_lines[i].strip()[-1] == ':':
                    char_name = file_lines[i][:-2]
                    i += 1
                    while i < len(file_lines) and file_lines[i] != '\n' and file_lines[i][0] != '[':
                        dc.run_scene(char_name, file_lines[i].strip(), char)
                        i += 1

                # If time to select drink and food
                elif file_lines[i] == '[SELECTION]\n':
                    # SELECTION
                    i += 1
                    we_want = literal_eval(file_lines[i])

                    drink_selection = ds.run_scene(we_want, vol)
                    fs.run_scene(we_want, vol)    

                # If time to make the drink
                elif file_lines[i] == '[MINIGAME]\n':
                    # MINIGAME
                    if drink_selection >= 4:
                        mm.run_scene(DRINK_COlORS[drink_selection], vol)
                    else:
                        mt.run_scene(DRINK_COlORS[drink_selection], vol)

        # End of game screen
        run = es.run_scene()

    pygame.quit()


if __name__ == "__main__":
    main()