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
TITLE_TEXT = pygame.transform.scale(pygame.image.load(os.path.join('../assets/title_seq', 'title.png')), 
                                    (WIDTH, HEIGHT))
START_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('../assets/title_seq', 'frame_' + 
                                        str(i) + '.png')), (WIDTH, HEIGHT)) for i in range(0,12)]
MAIN_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('../assets/title_seq', 'main_' + 
                                        str(i) + '.png')), (WIDTH, HEIGHT)) for i in range(0,3)]

# Define movement constants
FPS = 60

# Define colors
WHITE = (255,255,255)

pygame.display.set_caption("Comfort Cafe")

def draw_window():
    # update
    pygame.display.update()

def starting_animation(bg_counter):
    WIN.blit(START_GIF[bg_counter], (0,0))

def main_animation(i):
    WIN.blit(MAIN_GIF[i], (0,0))

def fade_in_text(text_opacity, selected_pos=None):
    if text_opacity < 255:
        trans_text = TITLE_TEXT.copy()
        trans_text.fill((255, 255, 255, text_opacity), None, pygame.BLEND_RGBA_MULT)
        WIN.blit(trans_text, (0,0))
    else:
        WIN.blit(TITLE_TEXT, (0,0))
        pygame.draw.rect(WIN, WHITE, selected_pos)

def main():
    # initialize clock
    clock = pygame.time.Clock()
    run = True

    elapsed_time_ctr = 0
    bg_counter = 0
    text_opacity = 5
    select_indicator = pygame.Rect(510, 200, 10, 10)

    # game loop
    while(run):
        clock.tick(FPS)

        t = clock.get_time()
        elapsed_time_ctr += t
        
        # Handle background
        if bg_counter < 12:
                starting_animation(bg_counter)
        else:
            main_animation(bg_counter%3)
            
        if elapsed_time_ctr >= 247.5:
            bg_counter += 1
            elapsed_time_ctr = 0

        # Handle Menu selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if text_opacity == 255:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        select_indicator = pygame.Rect(510, 200, 10, 10)

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        select_indicator = pygame.Rect(510, 270, 10, 10)
                        

        # Handle title text
        if bg_counter > 12:
            if text_opacity < 254:
                fade_in_text(text_opacity)
                text_opacity += 10
            else:
                fade_in_text(text_opacity, select_indicator)


        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()