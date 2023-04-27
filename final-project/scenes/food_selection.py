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
        # Define colors
        self.WHITE = (255,255,255)

    def draw_window(self, select_i):
        self.WIN.blit(self.SELECT_GRID[select_i], (0,0))

        # update
        pygame.display.update()


    def run_scene(self):
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
                        return select_i + 1

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