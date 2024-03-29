import pygame
import sys
from field import Field
import pickle


class Map:

    def __init__(self, screen):
        self.map = map
        self.screen = screen

        self.colors = {
                        "water": (0, 0, 255),  # Blue
                        "plains": (0, 255, 0),  # Green
                        "desert": (255, 255, 0)  # Yellow
                    }


    def load_map(self):
       with open('data/map1.pickle', 'rb') as f:
        self.map = pickle.load(f)

        self.draw_map()


    def draw_map(self):
        x = 0
        y = 0
        field_size = 100  # Assuming each field is a 100x100 square

        for row in self.map:
            for field in row:
                # Determine the color based on the field type
                color = self.colors.get(field.field_type, (0, 0, 0))
                
                # Draw the field rectangle
                pygame.draw.rect(self.screen, color, (x, y, field_size, field_size))

                # If a player is present in the field, draw a circle in the center
                if field.player_present:
                    # Calculate the center of the rectangle
                    center_x = x + field_size // 2
                    center_y = y + field_size // 2

                    # Circle color (RGB), you can customize this
                    circle_color = (255, 0, 0)  # Red, for example

                    # Circle radius
                    circle_radius = 20  # You can adjust this size

                    # Draw the circle
                    pygame.draw.circle(self.screen, circle_color, (center_x, center_y), circle_radius)

                # Move to the next field in the row
                x += field_size + 5
            # Move to the next row
            y += field_size + 5
            x = 0  # Reset x coordinate to the beginning of the row  
