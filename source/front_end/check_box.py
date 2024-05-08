import pygame

from dataclasses import dataclass

from source.auxiliary import BLACK, WHITE, RED


@dataclass
class CheckBox:
    _x: int
    _y: int
    _width: int
    _height: int
    _text: str
    _screen: pygame.Surface
    _is_checked: bool = False
    _font: pygame.font.Font = None
    _option: any = None

    def __post_init__(self):
        self._font = self._font or pygame.font.Font(None, 32)
        self._text_surface = self._font.render(self._text, True, BLACK)
        self._box = pygame.Rect(self._x, self._y, self._width, self._height)
        self.checkbox_group = None
        self._mouse_down = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if not event:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and not self._mouse_down:
            if self._box.collidepoint(event.pos):
                self.is_checked = not self.is_checked
                self._mouse_down = True
                if self.checkbox_group:
                    self.checkbox_group.uncheck_others(self)
        if event.type == pygame.MOUSEBUTTONUP:
            self._mouse_down = False

    def draw_check_box(self) -> None:
        self.redraw_box()
        self._screen.blit(self._text_surface,
                          (self._x + self._width + 10, self._y + (self._height - self._text_surface.get_height()) // 2))

    def redraw_box(self) -> None:
        pygame.draw.rect(self._screen, WHITE, self._box)
        pygame.draw.rect(self._screen, BLACK, self._box, 2)
        if self._is_checked:
            center = self._box.center
            pygame.draw.line(self._screen, RED, (center[0] - 10, center[1] - 10),
                             (center[0] + 10, center[1] + 10), 3)
            pygame.draw.line(self._screen, RED, (center[0] + 10, center[1] - 10),
                             (center[0] - 10, center[1] + 10), 3)

    @property
    def is_checked(self) -> bool:
        return self._is_checked

    @is_checked.setter
    def is_checked(self, value) -> None:
        changed = value != self._is_checked
        if changed:
            self._is_checked = value
            self.redraw_box()

    @property
    def option(self) -> any:
        return self._option
