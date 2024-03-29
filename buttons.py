import pygame
from map import Map

class Button:
    def __init__(self, x, y, width, height, text, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.screen = screen

        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.font = pygame.font.SysFont('Arial', 25)
        self.text_surf = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)
        self.screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.text


    