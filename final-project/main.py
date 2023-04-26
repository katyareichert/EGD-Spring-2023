import pygame
import numpy  as np
import random
import os

from scenes.title_sequence import TitleSequence
from scenes.counter_k import MainCounter

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define movement constants
FPS = 60

pygame.display.set_caption("Comfort Cafe")

def main():
   
   # Initialize all scenes
    ts = TitleSequence(WIN, WIDTH, HEIGHT, FPS)
    mc = MainCounter(WIN, WIDTH, HEIGHT, FPS)

    run = ts.run_scene()

    while(run):
        run = mc.run_scene()

    pygame.quit()


if __name__ == "__main__":
    main()