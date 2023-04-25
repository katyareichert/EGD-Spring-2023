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
BG = pygame.transform.scale(pygame.image.load(os.path.join('../assets/drink_select', 'frame_0.png')), 
                                    (WIDTH, HEIGHT))
SELECT_GRID = [pygame.transform.scale(pygame.image.load(os.path.join('../assets/drink_select', 'frame_' + 
                                        str(i) + '.png')), (WIDTH, HEIGHT)) for i in range(1,7)]
# 
# 0 1 2
# 3 4 5


# Define movement constants
FPS = 60

# Define colors
WHITE = (255,255,255)

pygame.display.set_caption("Comfort Cafe")

def draw_window(select_i):

    if select_i < 0:
        WIN.blit(BG, (0,0))
    else:
        WIN.blit(SELECT_GRID[select_i], (0,0))

    # update
    pygame.display.update()


def main():
    # initialize clock
    clock = pygame.time.Clock()
    run = True
    select_i = -1

    # game loop
    while(run):
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                
                # Start select mode
                if select_i == -1:
                    select_i += 1

                # Enter the minigame
                elif event.key == pygame.K_RETURN:
                    if select_i < 3:
                        # tumblr
                        pass
                    else:
                        # mug
                        pass

                # Move selection
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and select_i < 3:
                    select_i += 3
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and select_i > 2:
                    select_i -= 3
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and select_i%3 != 0:
                    select_i -= 1
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and select_i%3 != 2:
                    select_i += 1

                        
        draw_window(select_i)

    pygame.quit()


if __name__ == "__main__":
    main()