import pygame


class Input(object):
    def __init__(self) -> None:
        self.quit=False
        
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit=True