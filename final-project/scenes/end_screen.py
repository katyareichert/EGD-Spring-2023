import pygame
import os

class EndScreen:

    def __init__(self, win, width, height, fps, font) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps
        
        # Read in background images
        self.MAIN_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/end_screen', 'end_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,8)]
        
        # Define colors
        self.WHITE = (255,255,255)
        self.BROWN = (60,45,31)
        self.YELLOW = (234,196,146)

        # Define text
        self.SMALL_FONT = font
        self.TEXTS = [self.SMALL_FONT.render("Restart Game", 1, self.BROWN),
                      self.SMALL_FONT.render("Quit", 1, self.BROWN)
        ]
        
        self.TXT_RECTS = [self.TEXTS[0].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 190)),
                          self.TEXTS[1].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 220))
        ]

    def draw_window(self, bg_counter, selected_i):

        # Handle background
        self.WIN.blit(self.MAIN_GIF[bg_counter%8], (0,0))

        # Draw rectangles and circle
        pygame.draw.rect(self.WIN, self.YELLOW, self.TXT_RECTS[selected_i])

        # Draw text
        for i in range(len(self.TEXTS)):
            self.WIN.blit(self.TEXTS[i], self.TXT_RECTS[i])

        # update
        pygame.display.update()

    def run_scene(self):
        # initialize clock
        clock = pygame.time.Clock()
        run = True

        elapsed_time_ctr = 0
        bg_counter = 0
        selected_i = 0

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
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        # move option
                        if selected_i > 0:
                            selected_i -= 1
                        
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        # move option
                        if selected_i < len(self.TEXTS)-1:
                            selected_i += 1

                    if event.key == pygame.K_RETURN:
                        if selected_i == 0:
                            return True
                        else:
                            return False
                            
            self.draw_window(bg_counter, selected_i)

            # Animation Counter
            if elapsed_time_ctr >= 375:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = MainCounter(win, w, h, 60)

    mc.run_scene()