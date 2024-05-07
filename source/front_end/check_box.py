import pygame

from source.auxiliary import BLACK, WHITE, RED


class CheckBox:
    def __init__(self, x, y, width, height, text, screen, font=None, is_checked=False, option=None):
        self._x = x
        self._y = y
        self._width = width  # Width of the clickable area, not the text
        self._height = height
        self._text = text  # todo: Do we need to store this?
        self._screen = screen
        self._is_checked = is_checked
        self._font = font if font else pygame.font.Font(None, 32)  # todo: Do we need to store this?
        self._text_surface = self._font.render(text, True, (0, 0, 0))
        self._box = pygame.Rect(x, y, width, height)
        self._option = option
        self._checkbox_group = None
        self._mouse_down = False

    def handle_event(self, event):
        if not event:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and not self._mouse_down:
            if self._box.collidepoint(event.pos):
                # Toggle the checkbox state if the box area is clicked
                self._is_checked = not self._is_checked
                self._mouse_down = True
                # Notify the group (if part of one) about the state change (so others can uncheck themselves)
                if self._checkbox_group:
                    self._checkbox_group.handle_checkbox(self)

        if event.type == pygame.MOUSEBUTTONUP:
            self._mouse_down = False

    def draw(self):
        self.redraw_box()

        # Draw the text next to the box
        self._screen.blit(self._text_surface,
                          (self._x + self._width + 10, self._y + (self._height - self._text_surface.get_height()) // 2))

    def redraw_box(self):
        # If checked, draw an "X", otherwise just draw the box
        if self._is_checked:
            pygame.draw.rect(self._screen, WHITE, self._box)
            pygame.draw.rect(self._screen, BLACK, self._box, 2)  # Border for box
            center = self._box.center
            pygame.draw.line(self._screen, RED, (center[0] - 10, center[1] - 10),
                             (center[0] + 10, center[1] + 10), 3)
            pygame.draw.line(self._screen, RED, (center[0] + 10, center[1] - 10),
                             (center[0] - 10, center[1] + 10), 3)
        else:
            # Draw the white box with a black border
            pygame.draw.rect(self._screen, WHITE, self._box)
            pygame.draw.rect(self._screen, BLACK, self._box, 2)  # Border for box

    @property
    def is_checked(self):
        return self._is_checked

    @is_checked.setter
    def is_checked(self, new_value):
        self._is_checked = new_value

    @property
    def option(self):
        return self._option

    @property
    def checkbox_group(self):
        return self._checkbox_group

    @checkbox_group.setter
    def checkbox_group(self, value):
        self._checkbox_group = value
