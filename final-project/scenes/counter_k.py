import pygame
import numpy  as np
import random
import os

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Read in background images
MAIN_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('../assets/counter', 'girl' + 
                                        str(i) + '.png')), (WIDTH, HEIGHT)) for i in range(1,5)]

# Define movement constants
FPS = 60

# Define colors
WHITE = (255,255,255)

pygame.display.set_caption("Comfort Cafe")

def draw_window(bg_counter):

    # Handle background
    WIN.blit(MAIN_GIF[bg_counter%4], (0,0))

    # update
    pygame.display.update()

def main():
    # initialize clock
    clock = pygame.time.Clock()
    run = True

    elapsed_time_ctr = 0
    bg_counter = 0

    # game loop
    while(run):
        clock.tick(FPS)

        t = clock.get_time()
        elapsed_time_ctr += t
        
        # Handle Menu selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                        
        draw_window(bg_counter)

        if elapsed_time_ctr >= 320:
            bg_counter += 1
            elapsed_time_ctr = 0

    pygame.quit()


if __name__ == "__main__":
    main()