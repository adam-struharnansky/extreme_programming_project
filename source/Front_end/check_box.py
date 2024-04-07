import pygame

class CheckBox:
    def __init__(self, x, y, width, height, text, screen, font=None, is_checked=False, option=None):
        self.x = x
        self.y = y
        self.width = width  # Width of the clickable area, not the text
        self.height = height
        self.text = text
        self.screen = screen
        self.is_checked = is_checked
        self.font = font if font else pygame.font.Font(None, 32)
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        # Keep the box as the clickable area, which is exactly 50x50 pixels for the box
        self.box = pygame.Rect(x, y, width, height)
        self.option = option
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.box.collidepoint(event.pos):
                # Toggle the checkbox state if the box area is clicked
                self.is_checked = not self.is_checked
                # Notify the group (if part of one) about the state change
                if self.group:
                    self.group.handle_event(event, self)

    def draw(self):
        # If checked, draw an "X", otherwise just draw the box
        if self.is_checked:
            pygame.draw.rect(self.screen, (255, 255, 255), self.box)
            pygame.draw.rect(self.screen, (0, 0, 0), self.box, 2)  # Border for box
            center = self.box.center
            pygame.draw.line(self.screen, (255, 0, 0), (center[0] - 10, center[1] - 10), (center[0] + 10, center[1] + 10), 3)
            pygame.draw.line(self.screen, (255, 0, 0), (center[0] + 10, center[1] - 10), (center[0] - 10, center[1] + 10), 3)
        else:
            # Draw the white box with a black border
            pygame.draw.rect(self.screen, (255, 255, 255), self.box)
            pygame.draw.rect(self.screen, (0, 0, 0), self.box, 2)  # Border for box

        # Draw the text next to the box
        self.screen.blit(self.text_surface, (self.x + self.width + 10, self.y + (self.height - self.text_surface.get_height()) // 2))