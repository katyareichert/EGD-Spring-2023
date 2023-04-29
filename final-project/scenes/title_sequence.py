import pygame
import os

from scenes.options_page import OptionsPage

class TitleSequence:

    def __init__(self, win, width, height, fps, op) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps
        self.OP = op

        # Read in background images
        self.TITLE_TEXT = pygame.transform.scale(pygame.image.load(os.path.join('assets/title_seq', 'title.png')), 
                                            (self.WIDTH, self.HEIGHT))
        self.START_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/title_seq', 'frame_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,12)]
        self.MAIN_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/title_seq', 'main_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,3)]
        self.OUT_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/title_seq', 'fade_out_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,17)]

        # Define colors
        self.WHITE = (255,255,255)

    def draw_window(self, bg_counter, text_opacity, select_indicator):
        # Handle background
        if bg_counter < 12:
                self.WIN.blit(self.START_GIF[bg_counter], (0,0))
        else:
            self.WIN.blit(self.MAIN_GIF[bg_counter%3], (0,0))

        # Handle title text
        if bg_counter > 12:
            if text_opacity < 254:
                self.fade_in_text(text_opacity)
                text_opacity += 10
            else:
                self.fade_in_text(text_opacity, select_indicator)

        # update
        pygame.display.update()

        return text_opacity

    def fade_in_text(self, text_opacity, selected_pos=None):
        if text_opacity < 255:
            trans_text = self.TITLE_TEXT.copy()
            trans_text.fill((255, 255, 255, text_opacity), None, pygame.BLEND_RGBA_MULT)
            self.WIN.blit(trans_text, (0,0))
        else:
            self.WIN.blit(self.TITLE_TEXT, (0,0))
            pygame.draw.rect(self.WIN, self.WHITE, selected_pos)

    def run_scene(self):
        # initialize clock
        clock = pygame.time.Clock()
        run = True

        elapsed_time_ctr = 0
        bg_counter = 0
        text_opacity = 5
        select_indicator = pygame.Rect(510, 200, 10, 10)
        char = 0

        # game loop
        while(run):
            clock.tick(self.FPS)

            t = clock.get_time()
            elapsed_time_ctr += t
            
            # Handle Menu selection
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return (False, 0)

                if text_opacity == 255:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            select_indicator.update(510, 200, 10, 10)

                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            select_indicator.update(510, 270, 10, 10)

                        if event.key == pygame.K_RETURN:

                            if select_indicator.collidepoint(511, 201):
                                # Start the game

                                for i in range(len(self.OUT_GIF)):
                                    pygame.event.get()
                                    self.WIN.blit(self.OUT_GIF[i], (0,0))
                                    pygame.display.update()
                                    
                                    clock.tick(4)

                                return (True, char)
                            
                            elif select_indicator.collidepoint(511, 271):
                                # Show about screen
                                char = self.OP.run_scene()
  
            text_opacity = self.draw_window(bg_counter, text_opacity, select_indicator)

            if elapsed_time_ctr >= 247.5:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = TitleSequence(win, w, h)

    mc.run_scene()