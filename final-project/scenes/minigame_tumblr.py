import pygame
import numpy  as np
import random
import os

from scenes.draw_fill_line import dashed_line

class MinigameTumblr:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps

        # Define screen constants
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/minigame', 'tumblr.png')), 
                                         (self.WIDTH, self.HEIGHT))

        # Define movement constants
        self.FILL_RATE = 2

        # Message Pane
        self.MESS_WIDTH, self.MESS_HEIGHT = 300, 400
        self.MESSAGE_PANE = pygame.Surface((self.MESS_WIDTH,self.MESS_HEIGHT), pygame.SRCALPHA) 
        self.MESSAGE_PANE.fill((255,255,255, 0))      

        # Define drink things
        self.GLASS_HEIGHT, self.GLASS_WIDTH = 44*5, 300
        self.GLASS = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, self.HEIGHT//2 - 125,
                                 self.GLASS_WIDTH, self.GLASS_HEIGHT)

        # Define colors
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)

    def draw_window(self, pink_rect, yellow_rect, fill_status, quality_text, pink_line_val, yellow_line_val, yellow_start_height):
        
        # drink fill
        pygame.draw.rect(self.WIN, self.WHITE, self.GLASS)
        pygame.draw.rect(self.WIN, self.PINK, pink_rect)
        pygame.draw.rect(self.WIN, self.YELLOW, yellow_rect)
        
        # drawing overlay
        self.WIN.blit(self.BG, (0, 0))
        
        # fill line
        if fill_status < 3:
            dashed_line(self.WIN, self.PINK, (self.WIDTH//3, pink_line_val),
                        (2*self.WIDTH//3, pink_line_val),width=3)
        elif fill_status < 5:
            dashed_line(self.WIN, self.YELLOW, (self.WIDTH//3, yellow_line_val),
                        (2*self.WIDTH//3, yellow_line_val), width=3)

        # message pane
        if fill_status == 2 or fill_status == 5:
            self.WIN.blit(self.MESSAGE_PANE, (2*self.WIDTH//3 + 50, self.HEIGHT//2 - self.MESS_HEIGHT//2))

        # update
        pygame.display.update()

    def run_scene(self, colors):

        pink, yellow = colors

        self.PINK = pink
        self.YELLOW = yellow

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
        yellow_line_val = random.randint(135, pink_line_val - 10)

        fill_status = 0
        quality_text = 'moo moo'

        # game loop
        while(run):
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # check keystrokes
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if fill_status == 0 or fill_status == 3:
                            fill_status += 1      

                    if event.key == pygame.K_RETURN:
                        if fill_status == 2: 
                            fill_status += 1
                            quality_text = 'moo moo'

                        if fill_status == 5:
                            return 

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if fill_status == 1 or fill_status == 4:
                                fill_status += 1

            # fill animation
            if fill_status == 1:
                if pink_height <= self.GLASS_HEIGHT:
                    pink_rect = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, 
                                            self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height, 
                                            self.GLASS_WIDTH, pink_height)
                    pink_height += self.FILL_RATE
                else:
                    fill_status += 1
            
            if fill_status == 4:
                if yellow_height <= self.GLASS_HEIGHT:
                    yellow_rect = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, yellow_start_height - yellow_height,
                                                    self.GLASS_WIDTH, yellow_height)
                    yellow_height += self.FILL_RATE
                else:
                    fill_status += 1

            # done with filling pink?
            if fill_status == 2:

                # get how close to line
                distance_to_line = abs((self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height)-(pink_line_val))
                
                if distance_to_line <= 20:
                    quality_text = 'Perfect! This will add an extra bit of magic to their day!'
                elif distance_to_line <= 40:
                    quality_text = 'Nice! Way to get the job done!'
                else:
                    quality_text = 'Oops... Hopefully this won\'t ruin their day...'

                self.MESSAGE_PANE.fill((255,255,255,255)) 

                # set yellow level
                yellow_start_height = self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height + 2

            # done filling yellow?
            if fill_status == 5:

                # get how close to line
                distance_to_line = abs((yellow_start_height - yellow_height)-(yellow_line_val))
                
                if distance_to_line <= 20:
                    quality_text = 'Perfect! This will add an extra bit of magic to their day!'
                elif distance_to_line <= 40:
                    quality_text = 'Nice! Way to get the job done!'
                else:
                    quality_text = 'Oops... Hopefully this won\'t ruin their day...'

                self.MESSAGE_PANE.fill((255,255,255,255))

            self.draw_window(pink_rect, yellow_rect, fill_status, quality_text, pink_line_val, yellow_line_val, yellow_start_height)


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = MinigameTumblr(win, w, h)

    mc.run_scene(((91,61,43), (246,233,215)))