import pygame
import sys
from field import Field
import pickle


class Map:

    def __init__(self, screen):
        self.map = map
        self.screen = screen
        self.field_size = 100

        self.colors = {
                        "water": (0, 0, 255),  # Blue
                        "plains": (0, 255, 0),  # Green
                        "desert": (255, 255, 0)  # Yellow
                    }


    def load_map(self):
       with open('data/map1.pickle', 'rb') as f:
        self.map = pickle.load(f)

        #self.draw_map() nacitavanie mapy a jej kreslenie moc nesuvisi

    def draw(self):
        self.draw_map()
        self.draw_monsters()
        self.draw_player()

    def draw_player(self):
        for x, row in enumerate(self.map):
            for y, field in enumerate(row):
                # Determine the color based on the field type
                if field.player_present:
                    # Calculate the center of the rectangle
                    center_x = x * (self.field_size + 5) + self.field_size // 2
                    center_y = y * (self.field_size + 5) + self.field_size // 2

                    # Circle color (RGB), you can customize this
                    circle_color = (0, 255, 0)  # Green, for example

                    # Circle radius
                    circle_radius = 20  # You can adjust this size

                    # Draw the circle
                    pygame.draw.circle(self.screen, circle_color, (center_x, center_y), circle_radius)

    def draw_monsters(self):
        for x, row in enumerate(self.map):
            for y, field in enumerate(row):
                # Determine the color based on the field type
                if field.enemy_present:
                    # Calculate the center of the rectangle
                    center_x = x * (self.field_size + 5) + self.field_size // 2
                    center_y = y * (self.field_size + 5) + self.field_size // 2

                    # Circle color (RGB), you can customize this
                    circle_color = (255, 0, 0)  # Red, for example

                    # Circle radius
                    circle_radius = 20  # You can adjust this size

                    # Draw the circle
                    pygame.draw.circle(self.screen, circle_color, (center_x, center_y), circle_radius)

    def draw_map(self):
          # Assuming each field is a 100x100 square
        for x, row in enumerate(self.map):
            for y, field in enumerate(row):
                # Determine the color based on the field type
                color = self.colors.get(field.field_type, (0, 0, 0))
                
                # Draw the field rectangle
                pygame.draw.rect(self.screen, color, (x * (self.field_size + 5),
                                                      y * (self.field_size + 5),
                                                      self.field_size,
                                                      self.field_size))

