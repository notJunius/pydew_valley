import pygame
from settings import * 
from animator import create_frames
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        #info about spritesheet
        self.sprite_sheet = './Sprout Lands - Sprites - premium pack/Characters/Premium Charakter Spritesheet.png'
        self.sprite_rows = 24
        self.sprite_columns = 8
        self.sprite_width = 42
        self.sprite_height = 42
        self.scale = 8

        # additional state properties used for animation
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        #general setup, including scaling image to be bigger
        self.image = pygame.transform.scale(self.animations[self.status][self.frame_index], (self.sprite_width * self.scale, self.sprite_height * self.scale))
        self.rect = self.image.get_rect(center = pos)

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        #timers
        self.timers = {
            'tool use' : Timer(750, self.use_tool),
            'tool switch': Timer(100),
            'seed use': Timer(750, self.use_seed),
            'seed switch': Timer(100)
        }
        #tools
        self.tool_index = 0
        self.tools = ['axe', 'hoe', 'water']
        self.selected_tool = self.tools[self.tool_index]

        # seeds
        self.seeds = ['none', 'corn', 'carrot', 'cauliflower', 'tomato', 'eggplant', 'wheat', 'pumpkin', 'cucumber' ]
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]
    
    def use_tool(self):
        pass

    def use_seed(self):
        pass

    def import_assets(self):
        self.sprite_frames = create_frames(self.sprite_sheet, self.sprite_rows, self.sprite_columns)
        self.animations = {'down_idle': self.sprite_frames[0], 'up_idle' : self.sprite_frames[1], 'right_idle' : self.sprite_frames[2], 'left_idle' : self.sprite_frames[3], 
                            'down_walk' : self.sprite_frames[4], 'up_walk' : self.sprite_frames[5], 'right_walk' : self.sprite_frames[6], 'left_walk' : self.sprite_frames[7], 
                            'down_run' : self.sprite_frames[8], 'up_run' : self.sprite_frames[9], 'right_run' : self.sprite_frames[10], 'left_run' : self.sprite_frames[11], 
                            'down_hoe' : self.sprite_frames[12], 'up_hoe' : self.sprite_frames[13], 'right_hoe' : self.sprite_frames[14], 'left_hoe' : self.sprite_frames[15], 
                            'down_axe' : self.sprite_frames[16], 'up_axe' : self.sprite_frames[17], 'right_axe' : self.sprite_frames[18], 'left_axe' : self.sprite_frames[19], 
                            'down_water' : self.sprite_frames[20], 'up_water' : self.sprite_frames[21], 'right_water' : self.sprite_frames[22], 'left_water' : self.sprite_frames[23], }

    def animate(self, dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.status][int(self.frame_index)], (self.sprite_width * self.scale, self.sprite_height * self.scale))

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['tool use'].active:
            # Direction
            if keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
            if keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0
            
            # tool use
            if keys[pygame.K_SPACE]:
                #timer for tool use
                self.frame_index = 0
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2()
            
            if keys[pygame.K_f]:
                self.frame_index = 0
                self.timers['seed use'].activate()
                self.direction = pygame.math.Vector2()
            
            # change tool
            if keys[pygame.K_q] and not self.timers['tool switch'].active:
                if self.tool_index == 0:
                    self.timers['tool switch'].activate()
                    self.tool_index = len(self.tools) - 1
                    self.selected_tool = self.tools[self.tool_index]
                else: 
                    self.timers['tool switch'].activate()
                    self.tool_index -= 1
                    self.selected_tool = self.tools[self.tool_index]
            if keys[pygame.K_e] and not self.timers['tool switch'].active:
                if self.tool_index == len(self.tools) - 1:
                    self.timers['tool switch'].activate()
                    self.tool_index = 0
                    self.selected_tool = self.tools[self.tool_index]
                else: 
                    self.timers['tool switch'].activate()
                    self.tool_index += 1
                    self.selected_tool = self.tools[self.tool_index]
            
            # change seed
            if keys[pygame.K_z] and not self.timers['seed switch'].active:
                if self.seed_index == 0:
                    self.timers['seed switch'].activate()
                    self.seed_index = len(self.seeds) - 1
                    self.selected_seed = self.seeds[self.seed_index]
                    print(self.selected_seed)
                else: 
                    self.timers['seed switch'].activate()
                    self.seed_index -= 1
                    self.selected_seed = self.seeds[self.seed_index]
                    print(self.selected_seed)
            if keys[pygame.K_c] and not self.timers['seed switch'].active:
                if self.seed_index == len(self.seeds) - 1:
                    self.timers['seed switch'].activate()
                    self.seed_index = 0
                    self.selected_seed = self.seeds[self.seed_index]
                    print(self.selected_seed)
                else: 
                    self.timers['seed switch'].activate()
                    self.seed_index += 1
                    self.selected_seed = self.seeds[self.seed_index]
                    print(self.selected_seed)
                
    def get_status(self):
        key = pygame.key.get_pressed()
        
        # idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
            
        if (self.direction.magnitude() > 0) and key[pygame.K_LSHIFT]:
            self.status = self.status.split('_')[0] + '_run'
            self.speed = 300
        # walk
        elif self.direction.magnitude() > 0:
            self.status = self.status.split('_')[0] + '_walk'
            self.speed = 200

        # Tool use
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + f'_{self.selected_tool}'

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)