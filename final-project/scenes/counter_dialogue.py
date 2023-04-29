import pygame
import os

from scenes.helper_functions import DynamicText

class DialogueCounter:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps
        
        # Read in background images
        self.MAIN_GIF_k = [pygame.transform.scale(pygame.image.load(os.path.join('assets/counter', 'girl' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(1,5)]
        self.MAIN_GIF_j = [pygame.transform.scale(pygame.image.load(os.path.join('assets/counter', 'boy' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(1,5)]

        # Read in dialogue box
        self.DIA_BOX = pygame.transform.scale(pygame.image.load(os.path.join('assets/counter', 'dialogue_box.png')), 
                                            (137*5,34*5))
        self.DIA_BOX_RECT = self.DIA_BOX.get_rect(center=(self.WIDTH//2, 3*self.HEIGHT//4 + 10))

        # Define fonts
        self.NAME_FONT = pygame.font.SysFont('pixeloidsansjr6qo', 25)
        self.DIA_FONT = pygame.font.SysFont('pixeloidsansjr6qo', 20)

        # Define colors
        self.BROWN = (60,45,31)

    def draw_window(self, bg_counter):

        # Handle background
        self.WIN.blit(self.MAIN_GIF[bg_counter%4], (0,0))

        # Dialogue box
        self.WIN.blit(self.DIA_BOX, self.DIA_BOX_RECT)

        # Name text
        self.WIN.blit(self.NAME_TEXT, self.NAME_TEXT_RECT)

        # update
        pygame.display.update()

    def run_scene(self, char_name, dia_text, char=0):
        # initialize clock
        clock = pygame.time.Clock()
        run = True

        # initialize name text
        self.NAME_TEXT = self.NAME_FONT.render(char_name, 1, self.BROWN)
        self.NAME_TEXT_RECT = self.NAME_TEXT.get_rect(center=(22*5, 67*5))

        # initialize dialogue text
        message = DynamicText(self.DIA_FONT, "Alex", (13*5, 66*5), autoreset=True)
        # coordinates 17*5, 79*5

        if char:
            self.MAIN_GIF = self.MAIN_GIF_j
        else:
            self.MAIN_GIF = self.MAIN_GIF_k

        elapsed_time_ctr = 0
        bg_counter = 0

        # game loop
        while(run):
            clock.tick(self.FPS)

            t = clock.get_time()
            elapsed_time_ctr += t
            
            # Handle User Actions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                            
            self.draw_window(bg_counter)

            # Animation Counter
            if elapsed_time_ctr >= 375:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = MainCounter(win, w, h, 60)

    mc.run_scene()