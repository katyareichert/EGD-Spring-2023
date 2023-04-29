import pygame
import numpy  as np

def dashed_line(surface, color, start_pos, end_pos, width = 1, 
                     dash_length = 10, exclude_corners = True):

    # convert tuples to numpy arrays
    start_pos = np.array(start_pos)
    end_pos   = np.array(end_pos)

    # get euclidian distance between start_pos and end_pos
    length = np.linalg.norm(end_pos - start_pos)

    # get amount of pieces that line will be split up in (half of it are amount of dashes)
    dash_amount = int(length / dash_length)

    # x-y-value-pairs of where dashes start (and on next, will end)
    dash_knots = np.array([np.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]
                          ).transpose()

    return [pygame.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)
            for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]


# a simple class that uses the generator
# and can tell if it is done
class DynamicText(object):
    def __init__(self, font, text, pos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = self.text_generator(self.text)
        self.pos = pos
        self.autoreset = autoreset
        self.update()
    
        
    def text_generator(self, text):
        tmp = ''
        for letter in text:
                tmp += letter
                # don't pause for spaces
                if letter != ' ':
                        yield tmp

    def reset(self):
        self._gen = self.text_generator(self.text)
        self.done = False
        self.update()
        
    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (60,45,31))
            except StopIteration: 
                self.done = True
                if self.autoreset: self.reset()

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)