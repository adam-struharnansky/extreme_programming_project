import pygame

from dataclasses import dataclass

from source.auxiliary import BLACK, WHITE, GameState


@dataclass
class Button:
    _x: int
    _y: int
    _width: int
    _height: int
    _text: str
    _screen: pygame.Surface
    _response: GameState

    def __post_init__(self):
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
        self._font = pygame.font.SysFont('Arial', 25)
        self._text_surf = self._font.render(self._text, True, WHITE)
        self._text_rect = self._text_surf.get_rect(center=self._rect.center)

    def draw_button(self) -> None:
        pygame.draw.rect(self._screen, BLACK, self._rect)
        self._screen.blit(self._text_surf, self._text_rect)

    def get_response_to_event(self, event: pygame.event.Event) -> GameState | None:
        if not event:
            return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self._rect.collidepoint(event.pos):
                return self._response
        return None
