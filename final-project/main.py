import pygame
import numpy  as np
import random
import os

from draw_fill_line import dashed_line

pygame.font.init()
pygame.mixer.init()

# Define screen constants
WIDTH, HEIGHT = 150*5, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load(os.path.join('./assets/minigame', 'mug.png')), (WIDTH, HEIGHT))

# Define movement constants
FPS = 60
FILL_RATE = 2

# Text
HEALTH_FONT = pygame.font.SysFont('comicsans', 30)

# Message Pane
MESS_WIDTH = 300
MESS_HEIGHT = 400
MESSAGE_PANE = pygame.Surface((MESS_WIDTH, MESS_HEIGHT), pygame.SRCALPHA) 
MESSAGE_PANE.fill((255,255,255, 0))      

# Define drink things
GLASS_HEIGHT = 200
GLASS_WIDTH = 300
GLASS = pygame.Rect(WIDTH//2 - GLASS_WIDTH//2, HEIGHT//2 - GLASS_HEIGHT//2, GLASS_WIDTH, GLASS_HEIGHT)

# Define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
PINK = (255,192,203)
YELLOW = (255, 191, 0)

pygame.display.set_caption("Comfort Cafe")

def draw_window(pink_rect, yellow_rect, fill_status, quality_text, pink_line_val, yellow_line_val, yellow_start_height):
    # drink fill
    pygame.draw.rect(WIN, WHITE, GLASS)
    pygame.draw.rect(WIN, PINK, pink_rect)
    pygame.draw.rect(WIN, YELLOW, yellow_rect)
    
    # drawing overlay
    WIN.blit(BG, (0, 0))

    # fill line
    if fill_status < 3:
        dashed_line(WIN, PINK, (WIDTH//3, pink_line_val), (2*WIDTH//3, pink_line_val), width=3)
    elif fill_status < 5:
        dashed_line(WIN, YELLOW, (WIDTH//3, yellow_line_val), (2*WIDTH//3, yellow_line_val), width=3)

    # message pane
    if fill_status == 2:
        WIN.blit(MESSAGE_PANE, (2*WIDTH//3 + 50, HEIGHT//2 - MESS_HEIGHT//2))

    # TEST ----- fill_status counter
    red_health_text = HEALTH_FONT.render(str(fill_status), 1, WHITE)
    WIN.blit(red_health_text, (10, 10))

    red_health_text = HEALTH_FONT.render(str(quality_text), 1, WHITE)
    WIN.blit(red_health_text, (10, 30))

    # update
    pygame.display.update()

def main():
    # initialize clock
    clock = pygame.time.Clock()
    run = True

    # initialize pink drink variables
    pink_height = 2
    pink_rect = pygame.Rect(0, 0, 0, 0)

    # initialize yellow drink variables
    yellow_start_height = 200
    yellow_height = 2
    yellow_rect = pygame.Rect(0, 0, 0, 0)

    # get random line levels
    pink_line_val = random.randint(220, 280)
    yellow_line_val = random.randint(180, pink_line_val - 10)

    fill_status = 0
    quality_text = 'moo moo'

    CONT_BUTTON = WIN.blit(pygame.Surface((0, 0), pygame.SRCALPHA), (0, 0))

    # game loop
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # check keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if fill_status == 0 or fill_status == 3:
                        fill_status += 1      

                if event.key == pygame.K_RETURN:
                    if fill_status == 2: 
                        fill_status += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if fill_status == 1 or fill_status == 4:
                            fill_status += 1

            # check mouse action
            if event.type == pygame.MOUSEBUTTONDOWN:
                b = CONT_BUTTON
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos):
                    fill_status += 1
                    CONT_BUTTON = pygame.Rect(0,0,0,0)

        # fill animation
        if fill_status == 1:
            if pink_height <= GLASS_HEIGHT:
                pink_rect = pygame.Rect(WIDTH//2 - GLASS_WIDTH//2, HEIGHT//2 + GLASS_HEIGHT//2 - 
                                              pink_height, GLASS_WIDTH, pink_height)
                pink_height += FILL_RATE
            else:
                fill_status += 1
        
        if fill_status == 4:
            if yellow_height <= GLASS_HEIGHT:
                yellow_rect = pygame.Rect(WIDTH//2 - GLASS_WIDTH//2, yellow_start_height - yellow_height,
                                                GLASS_WIDTH, yellow_height)
                yellow_height += FILL_RATE
            else:
                fill_status += 1

        # done with filling pink?
        if fill_status == 2:

            # get how close to line
            distance_to_line = abs((HEIGHT//2 + GLASS_HEIGHT//2 - pink_height)-(pink_line_val))
            
            if distance_to_line <= 20:
                quality_text = 'Great job! This will add an extra bit of magic to their day!'
            elif distance_to_line <= 40:
                quality_text = 'Nice! Way to get the job done!'
            else:
                quality_text = 'Oops... Hopefully this ruin their day...'

            MESSAGE_PANE.fill((255,255,255,255)) 

            # set yellow level
            yellow_start_height = HEIGHT//2 + GLASS_HEIGHT//2 - pink_height + 2

        # done filling yellow?
        if fill_status == 5:

            # get how close to line
            distance_to_line = abs((HEIGHT//2 + GLASS_HEIGHT//2 - yellow_height)-(yellow_line_val))
            
            if distance_to_line <= 20:
                quality_text = 'Great job! This will add an extra bit of magic to their day!'
            elif distance_to_line <= 40:
                quality_text = 'Nice! Way to get the job done!'
            else:
                quality_text = 'Oops... Hopefully this ruin their day...'

            MESSAGE_PANE.fill((255,255,255,255))

        draw_window(pink_rect, yellow_rect, fill_status, quality_text, pink_line_val, yellow_line_val, yellow_start_height)

    pygame.quit()


if __name__ == "__main__":
    main()