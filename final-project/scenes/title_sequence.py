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
CREDIT_PAGE = pygame.transform.scale(pygame.image.load(os.path.join('../assets/title_seq', 'credits.png')), 
                                    (WIDTH, HEIGHT))

# Define movement constants
FPS = 60

# Define colors
WHITE = (255,255,255)

pygame.display.set_caption("Comfort Cafe")

def draw_window(show_credits_page, bg_counter, text_opacity, select_indicator):

    if show_credits_page:
         WIN.blit(CREDIT_PAGE, (0,0))

    else:
        # Handle background
        if bg_counter < 12:
                WIN.blit(START_GIF[bg_counter], (0,0))
        else:
            WIN.blit(MAIN_GIF[bg_counter%3], (0,0))

        # Handle title text
        if bg_counter > 12:
            if text_opacity < 254:
                fade_in_text(text_opacity)
                text_opacity += 10
            else:
                fade_in_text(text_opacity, select_indicator)

    # update
    pygame.display.update()

    return text_opacity

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
    show_credits_page = False

    # game loop
    while(run):
        clock.tick(FPS)

        t = clock.get_time()
        elapsed_time_ctr += t
        
        # Handle Menu selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if text_opacity == 255:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        select_indicator.update(510, 200, 10, 10)

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        select_indicator.update(510, 270, 10, 10)

                    if event.key == pygame.K_RETURN:
                        if show_credits_page == True:
                            show_credits_page = False
                        elif select_indicator.collidepoint(511, 201):
                            # Start the game
                            pass
                        elif select_indicator.collidepoint(511, 271):
                            # Show about screen
                            show_credits_page = True

                        
        text_opacity = draw_window(show_credits_page, bg_counter, text_opacity, select_indicator)

        if elapsed_time_ctr >= 247.5:
            bg_counter += 1
            elapsed_time_ctr = 0

    pygame.quit()


if __name__ == "__main__":
    main()