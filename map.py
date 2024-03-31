import pygame
import sys
from field import Field
from player import Player
import pickle


class Map:

    class Data():
        def __init__(self):
            self.map = None
            self.field_size = 100
            self.player_pos = [0,0] #X, Y
            self.player = Player()

    def __init__(self, screen, stat_tab, file = 'data/map0.pickle'):                
        self.dat = self.Data()
        self.screen = screen
        self.stat_tab = stat_tab
        self.file = file
        font = pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 30)

        
        self.colors = {
                        "water": (0, 0, 255),  # Blue
                        "plains": (0, 255, 0),  # Green
                        "desert": (255, 255, 0)  # Yellow
                    }
        self.background_color = (255, 255, 255)

    def save_map(self, file = None):
        if file == None:
            file = self.file
        with open(file, 'wb') as f:
            pickle.dump(self.dat,f)

    def load_map(self, file = None):
        if file == None:
            file = self.file
        with open(file, 'rb') as f:
            self.dat = pickle.load(f)

    def move(self, direction):
        match direction:
            case 1073741903:
                self.dat.player_pos[0] += 1
            case 1073741904:
                self.dat.player_pos[0] -= 1
            case 1073741905:
                self.dat.player_pos[1] += 1
            case 1073741906:
                self.dat.player_pos[1] -= 1

        if self.dat.player_pos[0] < 0:
            self.dat.player_pos[0] = 0

        if self.dat.player_pos[1] < 0:
            self.dat.player_pos[1] = 0
            #todo, skontroluj ci tu je spravne X a Y max dlzka pola
        if self.dat.player_pos[0] >= len(self.dat.map[0]):
            self.dat.player_pos[0] = len(self.dat.map[0]) - 1

        if self.dat.player_pos[1] >= len(self.dat.map):
            self.dat.player_pos[1] = len(self.dat.map) - 1

        
        
        #self.draw_map() nacitavanie mapy a jej kreslenie moc nesuvisi

    def draw(self):
        self.screen.fill(self.background_color)
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

        #===================================================
        text = ""
        text += "Att: " + str(self.dat.player.get_attack())
        text += " | Def: " + str(self.dat.player.get_defence())
        text += " | Evs: " + str(self.dat.player.get_evasion())
        text += " | Spd: " + str(self.dat.player.get_speed())
        text += " | Lvl: " + str(self.dat.player.get_level())
        text += " | XP: " + str(self.dat.player.get_defence()) + "/" + str(self.dat.player.get_next_level_experience())
        text += " | HP: " + str(self.dat.player.get_health()) + "/" + str(self.dat.player.get_max_health())
        text_surface = self.font.render(text, False, (255, 255, 255))
        self.stat_tab.blit(text_surface, (10,5))

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

