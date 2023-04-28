import pygame
import os

class OptionsPage:

    def __init__(self, win, width, height, fps, volume, font1, font2, char='k') -> None:

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
        # Define colors
        self.WHITE = (255,255,255)
        self.BROWN = (60,45,31)

        # Define fonts
        self.BIG_FONT = font1
        self.SMALL_FONT = font2
        
        self.VOL_TXT = self.BIG_FONT.render("Volume", 1, self.BROWN)
        self.CHAR_TXT = self.BIG_FONT.render("Character", 1, self.BROWN)
        self.RETURN_TXT = self.SMALL_FONT.render("Return to Game", 1, self.BROWN)
        self.EXIT_TXT = self.SMALL_FONT.render("Quit Game", 1, self.BROWN)

        self.VOL_RECT = self.VOL_TXT.get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2))
        self.CHAR_RECT = self.CHAR_TXT.get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 100))
        self.RETURN_RECT = self.RETURN_TXT.get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 200))
        self.EXIT_RECT = self.EXIT_TXT.get_rect(center=(self.WIDTH//2 + 10, self.HEIGHT//2 + 230))

    def draw_window(self, bg_counter):

        # Draw background
        self.WIN.blit(self.CREDIT_PAGE, (0,0))
        self.WIN.blit(self.CREDIT_GIF[bg_counter%8], (0,0))

        # Draw text
        self.WIN.blit(self.VOL_TXT, self.VOL_RECT)
        self.WIN.blit(self.CHAR_TXT, self.CHAR_RECT)
        self.WIN.blit(self.RETURN_TXT, self.RETURN_RECT)
        self.WIN.blit(self.EXIT_TXT, self.EXIT_RECT)

        # update
        pygame.display.update()

    def run_scene(self):
        # initialize clock
        clock = pygame.time.Clock()
        run = True

        elapsed_time_ctr = 0
        bg_counter = 0

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
                        pass

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        # move option
                        pass

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        # change volume or select character
                        self.VOLUME = round(self.VOLUME - 0.2, 1)
                        pygame.mixer.music.set_volume(self.VOLUME)

                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        # change volume or select character
                        self.VOLUME = round(self.VOLUME + 0.2, 1)
                        pygame.mixer.music.set_volume(self.VOLUME)

                    if event.key == pygame.K_RETURN:
                        return
  
            self.draw_window(bg_counter)

            if elapsed_time_ctr >= 375:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = OptionsPage(win, w, h)

    mc.run_scene()