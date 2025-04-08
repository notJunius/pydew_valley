import pygame
from settings import *
from animator import create_frames
class Overlay:
    def __init__(self, player):
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.import_assets()
        self.icon_width = 16
        self.scale = 4
    

    def import_assets(self):
        #imports
        self.icons = create_frames('./Sprout Lands - Sprites - premium pack/Objects/Items/items-spritesheet.png', 15, 8)
        self.tools_surf = {'hoe' : self.icons[0][3], 'axe' : self.icons[0][2], 'water' : self.icons[1][2]}
        self.seeds_surf = {'carrot' : self.icons[2][0], 'tomato' :self.icons[4][0], 'none' : self.icons[0][0]}

    def display(self):

        # tool
        tool_surf = pygame.transform.scale(self.tools_surf[self.player.selected_tool], (self.icon_width * self.scale, self.icon_width * self.scale))
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rect)

        # seeds
        seed_surf = pygame.transform.scale(self.seeds_surf[self.player.selected_seed], (self.icon_width * self.scale, self.icon_width * self.scale))
        seed_rect = seed_surf.get_rect(midbottom = OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)
