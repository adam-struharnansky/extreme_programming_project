import pygame

from source.auxiliary import BLACK, WHITE


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, screen: pygame.Surface) -> None:
        """
        Create a button with given parameters on the screen
        :param x: Left-most point of the button
        :param y: Upper-most point of the button
        :param width: Width of the button
        :param height: Height of the button
        :param text: Text displayed on the button
        :param screen: Screen on which the button will be placed
        """
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._text = text
        self._screen = screen

        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        self._font = pygame.font.SysFont('Arial', 25)
        self._text_surf = self._font.render(self._text, True, WHITE)
        self._text_rect = self._text_surf.get_rect(center=self._rect.center)

    def draw(self):
        pygame.draw.rect(self._screen, BLACK, self._rect)
        self._screen.blit(self._text_surf, self._text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                return self._text
