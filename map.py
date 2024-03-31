import pygame
import sys
from field import Field
import pickle


class Map:

    class Data():
        def __init__(self):
            self.map = None
            self.field_size = 100
            self.player_pos = [0,0]

    def __init__(self, screen, file = 'data/map0.pickle'):                
        self.dat = None
        self.screen = screen
        self.file = file

        self.colors = {
                        "water": (0, 0, 255),  # Blue
                        "plains": (0, 255, 0),  # Green
                        "desert": (255, 255, 0)  # Yellow
                    }

    def save_map(self, file = None):
        if file == None:
            file = self.file
        with open(file, 'wb') as f:
            pickle.dump(self.data,f)

    def load_map(self, file = None):
        if file == None:
            file = self.file
        with open(file, 'rb') as f:
            self.dat = pickle.load(f)
        
        #self.draw_map() nacitavanie mapy a jej kreslenie moc nesuvisi

    def draw(self):
        self.draw_map()
        self.draw_monsters()
        self.draw_player()

    def draw_player(self):
        x, y = self.dat.player_pos
        field_size = self.dat.field_size
        
        center_x = x * (field_size + 5) + field_size // 2
        center_y = y * (field_size + 5) + field_size // 2

        #Circle color (RGB), you can customize this
        circle_color = (0, 255, 0)  # Green, for example

        # Circle radius
        circle_radius = 20  # You can adjust this size

        # Draw the circle
        pygame.draw.circle(self.screen, circle_color, (center_x, center_y), circle_radius)

    def draw_monsters(self):
        field_size = self.dat.field_size
        for x, row in enumerate(self.dat.map):
            for y, field in enumerate(row):
                # Determine the color based on the field type
                if field.enemy_present:
                    # Calculate the center of the rectangle
                    center_x = x * (field_size + 5) + field_size // 2
                    center_y = y * (field_size + 5) + field_size // 2

                    # Circle color (RGB), you can customize this
                    circle_color = (255, 0, 0)  # Red, for example

                    # Circle radius
                    circle_radius = 20  # You can adjust this size

                    # Draw the circle
                    pygame.draw.circle(self.screen, circle_color, (center_x, center_y), circle_radius)

    def draw_map(self):
        field_size = self.dat.field_size
          # Assuming each field is a 100x100 square
        for x, row in enumerate(self.dat.map):
            for y, field in enumerate(row):
                # Determine the color based on the field type
                color = self.colors.get(field.field_type, (0, 0, 0))
                
                # Draw the field rectangle
                pygame.draw.rect(self.screen, color, (x * (field_size + 5),
                                                      y * (field_size + 5),
                                                      field_size,
                                                      field_size))

