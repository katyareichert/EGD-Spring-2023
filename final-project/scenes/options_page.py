import pygame
import os

class OptionsPage:

    def __init__(self, win, width, height, fps, volume, font1, font2, char=0) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps

        # Define options
        self.VOLUME = volume
        self.CHAR = char

        # Read in background images
        self.CREDIT_PAGE = pygame.transform.scale(pygame.image.load(os.path.join('assets/options', 'credits.png')), 
                                            (self.WIDTH, self.HEIGHT))
        self.CREDIT_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/options', 'joey_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,8)]
        self.CIRCLES = [pygame.image.load(os.path.join('assets/options', 'circle_' +  str(i) + '.png')) for i in range(0,2)]
        
        # Define colors
        self.WHITE = (255,255,255)
        self.BROWN = (60,45,31)
        self.YELLOW = (234,196,146)

        # Define text
        self.BIG_FONT = font1
        self.SMALL_FONT = font2
        
        self.TEXTS = [self.BIG_FONT.render("Volume", 1, self.BROWN),
                      self.BIG_FONT.render("Character", 1, self.BROWN),
                      self.SMALL_FONT.render("Return to Game", 1, self.BROWN),
                      self.SMALL_FONT.render("Quit Game", 1, self.BROWN)
        ]
        
        self.TXT_RECTS = [self.TEXTS[0].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2)),
                          self.TEXTS[1].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 100)),
                          self.TEXTS[2].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 190)),
                          self.TEXTS[3].get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 220))
        ]


    def draw_window(self, bg_counter, selected_i):

        # Draw background
        self.WIN.blit(self.CREDIT_PAGE, (0,0))

        # Draw rectangle and circle
        pygame.draw.rect(self.WIN, self.YELLOW, self.TXT_RECTS[selected_i])
        self.WIN.blit(self.CIRCLES[self.CHAR], (0,0))

        # Draw characters
        self.WIN.blit(self.CREDIT_GIF[bg_counter%8], (0,0))

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
            
            # Handle Menu selection
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

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        # change volume or select character
                        if selected_i == 0:
                            self.VOLUME = round(self.VOLUME - 0.2, 1)
                            pygame.mixer.music.set_volume(self.VOLUME)
                        elif selected_i == 1:
                            self.CHAR = 1

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        # change volume or select character
                        if selected_i == 0:
                            self.VOLUME = round(self.VOLUME + 0.2, 1)
                            pygame.mixer.music.set_volume(self.VOLUME)
                        elif selected_i == 1:
                            self.CHAR = 0

                    if event.key == pygame.K_RETURN:
                        if selected_i < len(self.TEXTS)-2:
                            selected_i += 1
                        elif selected_i == len(self.TEXTS)-2:
                            return self.CHAR
                        else:
                            pygame.quit()
                            exit()
  
            self.draw_window(bg_counter, selected_i)

            if elapsed_time_ctr >= 375:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = OptionsPage(win, w, h)

    mc.run_scene()