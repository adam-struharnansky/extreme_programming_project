import pygame


class Button:
    def __init__(self, x, y, width, height, text, screen):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._text = text
        self._screen = screen

        self._rect = pygame.Rect(self._x, self._y, width, height)
        self._font = pygame.font.SysFont('Arial', 25)
        self._text_surf = self._font.render(self._text, True, (255, 255, 255))
        self._text_rect = self._text_surf.get_rect(center=self._rect.center)

    def draw(self):
        pygame.draw.rect(self._screen, (0, 0, 0), self._rect)
        self._screen.blit(self._text_surf, self._text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                return self._text
