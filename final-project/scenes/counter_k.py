import pygame
import os

class MainCounter:

    def __init__(self, win, width, height, fps) -> None:

        self.WIDTH, self.HEIGHT = width, height
        self.WIN = win
        self.FPS = fps
        
        # Read in background images
        self.MAIN_GIF = [pygame.transform.scale(pygame.image.load(os.path.join('assets/counter', 'girl' + 
                                                str(i) + '.png')), (self.WIDTH, self.HEIGHT)) for i in range(1,5)]

        # Define colors
        self.WHITE = (255,255,255)

    def draw_window(self, bg_counter):

        # Handle background
        self.WIN.blit(self.MAIN_GIF[bg_counter%4], (0,0))

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
            
            # Handle User Actions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True
                            
            self.draw_window(bg_counter)

            # Animation Counter
            if elapsed_time_ctr >= 320:
                bg_counter += 1
                elapsed_time_ctr = 0


if __name__ == "__main__":
    w,h = 150*5, 500
    win = pygame.display.set_mode((w, h))
    mc = MainCounter(win, w, h)

    mc.run_scene()