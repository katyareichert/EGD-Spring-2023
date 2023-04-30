import pygame
import numpy  as np
import random
import os

from scenes.helper_functions import dashed_line

class MinigameTumblr:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps
        self.FONT = pygame.font.SysFont('pixeloidsansjr6qo', 35)

        # Define screen constants
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join('assets/minigame', 'tumblr.png')), 
                                         (self.WIDTH, self.HEIGHT))
        self.STARS = pygame.transform.scale(pygame.image.load(os.path.join('assets/minigame', 'tumblr.png')), 
                                         (self.WIDTH, self.HEIGHT))

        # Define movement constants
        self.FILL_RATE = 2

        # Message Pane
        self.MESS_WIDTH, self.MESS_HEIGHT = 83*5, 14*5
        self.MESSAGE_PANE = pygame.Surface((self.MESS_WIDTH, self.MESS_HEIGHT), pygame.SRCALPHA)
        self.MESSAGE_PANE.fill((255,255,255, 0))   
        self.MESS_RECT = self.MESSAGE_PANE.get_rect(center=(self.WIDTH//2, 87*5))  

        # Define drink things
        self.GLASS_HEIGHT, self.GLASS_WIDTH = 44*5, 300
        self.GLASS = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, self.HEIGHT//2 - 125,
                                 self.GLASS_WIDTH, self.GLASS_HEIGHT)
        
        # Define sounds
        self.POURING_SOUND = pygame.mixer.Sound(os.path.join('sound', 'pouring.wav'))
        self.WIN_SOUND = pygame.mixer.Sound(os.path.join('sound', 'perfect.mp3'))
        self.OOPS_SOUND = pygame.mixer.Sound(os.path.join('sound', 'oops.mp3'))

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
            qt = self.FONT.render(quality_text, 1, self.BLACK)
            self.MESSAGE_PANE.blit(qt, qt.get_rect(center=(self.MESS_WIDTH//2, self.MESS_HEIGHT//2)))
            self.WIN.blit(self.MESSAGE_PANE, self.MESS_RECT)

        # update
        pygame.display.update()

    def done_filling_pink(self, pink_height, pink_line_val, quality_score):

         # get how close to line
        distance_to_line = abs((self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height)-(pink_line_val))
        self.MESSAGE_PANE.fill((241,216,181,255)) 

        # evaluate the distance
        quality_text, quality_score = self.evaluate_distance(distance_to_line, quality_score)

        return (self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height + 2, quality_text, quality_score)

    def done_filling_yellow(self, yellow_start_height, yellow_height, yellow_line_val, quality_score):

        # get how close to line
        distance_to_line = abs((yellow_start_height - yellow_height)-(yellow_line_val))
        self.MESSAGE_PANE.fill((241,216,181,255)) 

        return self.evaluate_distance(distance_to_line, quality_score)

    def evaluate_distance(self, distance_to_line, quality_score):

        if distance_to_line <= 20:
            quality_text = 'Perfect!'
            quality_score += 2
            self.WIN_SOUND.play()
        elif distance_to_line <= 40:
            quality_text = 'Nice!'
            quality_score += 1
            self.WIN_SOUND.play()
        else:
            quality_text = 'Oops...'
            self.OOPS_SOUND.play()

        return (quality_text, quality_score)

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
        yellow_line_val = random.randint(135, pink_line_val - 50)

        fill_status = 0
        quality_score = 2
        quality_text = 'moo moo'

        elapsed_time_ctr = 0

        # game loop
        while(run):
            clock.tick(self.FPS)

            # Run timer for quality text
            if fill_status == 2 or fill_status == 5:
                t = clock.get_time()
                elapsed_time_ctr += t

            # Check user actions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # check keystrokes
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if fill_status == 0 or fill_status == 3:
                            fill_status += 1      
                            self.POURING_SOUND.play()

                    if event.key == pygame.K_RETURN:
                        if fill_status == 2: 
                            elapsed_time_ctr = 0
                            fill_status += 1
                            quality_text = 'moo moo'

                        if fill_status >= 5:
                            return 

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:

                        self.POURING_SOUND.stop()
                        
                        if fill_status == 1:
                            yellow_start_height, quality_text, quality_score = self.done_filling_pink(pink_height, pink_line_val, quality_score)
                        if fill_status == 4:
                            quality_text, quality_score = self.done_filling_yellow(yellow_start_height, yellow_height, yellow_line_val, quality_score)

                        if fill_status == 1 or fill_status == 4:
                            fill_status += 1

            # Pink fill animation
            if fill_status == 1:
                if pink_height <= self.GLASS_HEIGHT:
                    pink_rect = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, 
                                            self.HEIGHT//2 - 125 + self.GLASS_HEIGHT - pink_height, 
                                            self.GLASS_WIDTH, pink_height)
                    pink_height += self.FILL_RATE
                else:
                    fill_status += 1
                    yellow_start_height, quality_text, quality_score = self.done_filling_pink(pink_height, pink_line_val, quality_score)
            
            # Yellow fill animation
            if fill_status == 4:
                if yellow_height <= self.GLASS_HEIGHT:
                    yellow_rect = pygame.Rect(self.WIDTH//2 - self.GLASS_WIDTH//2, yellow_start_height - yellow_height,
                                                    self.GLASS_WIDTH, yellow_height)
                    yellow_height += self.FILL_RATE
                else:
                    fill_status += 1
                    quality_text, quality_score = self.done_filling_yellow(yellow_start_height, yellow_height, yellow_line_val, quality_score)

            # Wait for score to go away
            if elapsed_time_ctr >= 3000:
                if fill_status == 2: 
                    elapsed_time_ctr = 0
                    fill_status += 1
                    quality_text = 'moo moo'

                if fill_status >= 5:
                    return 

            self.draw_window(pink_rect, yellow_rect, fill_status, quality_text, pink_line_val, yellow_line_val, yellow_start_height)


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = MinigameTumblr(win, w, h)

    mc.run_scene(((91,61,43), (246,233,215)))