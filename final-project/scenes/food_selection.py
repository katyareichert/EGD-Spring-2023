import pygame
import os

class FoodSelection:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps

        # Read in background images
        self.SELECT_GRID = [pygame.transform.scale(pygame.image.load(os.path.join('assets/food_select', 'frame_' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(1,7)]
        
        self.STAR_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/stars', 'star_' + 
                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(0,14)]

        # Define dialogue box
        self.FONT = pygame.font.SysFont('pixeloidsansjr6qo', 25)
        self.DIA_BOX = pygame.transform.scale(pygame.image.load(os.path.join('assets/counter', 'dialogue_box.png')), 
                                (137*5,34*5))
        self.DIA_BOX_RECT = self.DIA_BOX.get_rect(center=(self.WIDTH//2, 3*self.HEIGHT//4 + 10))
        self.NAME_TEXT = self.FONT.render('Alex', 1, (60,45,31))
        self.NAME_TEXT_RECT = self.NAME_TEXT.get_rect(center=(22*5, 67*5))
        self.MESSAGE = self.FONT.render('Maybe there is something better...', 1, (60,45,31))
        
        # Define colors
        self.WHITE = (255,255,255)

    def draw_window(self, select_i):
        self.WIN.blit(self.SELECT_GRID[select_i], (0,0))

        # update
        pygame.display.update()


    def run_scene(self, we_want):
        # initialize clock
        clock = pygame.time.Clock()
        run = True
        select_i = 0

        # game loop
        while(run):
            clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:

                    # Return food selected
                    if event.key == pygame.K_RETURN:

                        drink_selection = select_i + 1

                        if drink_selection in we_want:
                            # star animation
                            for i in range(len(self.STAR_GIF)):
                                pygame.event.get()
                                self.WIN.blit(self.SELECT_GRID[select_i], (0,0))
                                self.WIN.blit(self.STAR_GIF[i], (0,0))
                                pygame.display.update()
                                
                                clock.tick(6)
                            
                            return

                        else: 
                            
                            show_message = True
                            while show_message:
                                self.WIN.blit(self.DIA_BOX, self.DIA_BOX_RECT)
                                self.WIN.blit(self.NAME_TEXT, self.NAME_TEXT_RECT)
                                self.WIN.blit(self.MESSAGE, (14*5, 78*5))
                                pygame.display.update()

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        exit()
                                    elif event.type == pygame.KEYDOWN:
                                        show_message = False

                    # Move selection
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and select_i < 3:
                        select_i += 3
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and select_i > 2:
                        select_i -= 3
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and select_i%3 != 0:
                        select_i -= 1
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and select_i%3 != 2:
                        select_i += 1

                            
            self.draw_window(select_i)


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = FoodSelection(win, w, h)

    mc.run_scene()