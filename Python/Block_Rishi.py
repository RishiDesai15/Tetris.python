import pygame
class Block():
    def __init__(self, colour, gridxpos, gridypos):
        self.colour = colour # the colour
        self.gridxpos = int(gridxpos) # the x position
        self.gridypos = int(gridypos) # the y position
        self.size = 25 # the size of the block

    def draw(self, screen, player2):
        # draw a red rectangle on the screen
        padding=0
        if player2==True:
            padding=650
        pygame.draw.rect(screen, self.colour, [self.gridxpos*self.size+padding, self.gridypos*self.size, self.size-1, self.size-1], 0)