import pygame
import numpy  as np
import random
import os

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# BG = pygame.transform.scale(pygame.image.load(os.path.join('../assets/minigame', 'tumblr.png')), (WIDTH, HEIGHT))

# Define movement constants
FPS = 60

pygame.display.set_caption("Comfort Cafe")

def draw_window(bg_counter, text_opacity):
    
    # draw background
    # WIN.blit(BG, (0, 0))
    
    # update
    pygame.display.update()

def background_animation(bg_counter):
    if bg_counter < 20:
        WIN.blit()
    bg_counter += 1


def main():
    # initialize clock
    clock = pygame.time.Clock()
    run = True

    elapsed_time_ctr = 0
    bg_counter = 0
    text_opacity = 0

    # game loop
    while(run):
        clock.tick(FPS)

        t = clock.get_time()
        elapsed_time_ctr += t
        
        if elapsed_time_ctr >= 16.5*15:
            background_animation(bg_counter)

            if bg_counter < 20:
                bg_counter += 1

            elapsed_time_ctr = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()