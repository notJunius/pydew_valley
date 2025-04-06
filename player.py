import pygame
from settings import * 
from animator import create_frames

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        #info about spritesheet
        self.sprite_sheet = './Sprout Lands - Sprites - premium pack/Characters/Premium Charakter Spritesheet.png'
        self.sprite_rows = 24
        self.sprite_columns = 9
        sprite_width = 42
        sprite_height = 42


        self.import_assets()
        self.status = 'down_axe'
        self.frame_index = 0

        #general setup
        self.image = pygame.transform.scale(self.animations[self.status][self.frame_index], (sprite_width * 4, sprite_height * 4))
        self.rect = self.image.get_rect(center = pos)

        #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.sprite_frames = create_frames(self.sprite_sheet, self.sprite_rows, self.sprite_columns)
        self.animations = {'down_idle': self.sprite_frames[0], 'up_idle' : self.sprite_frames[1], 'right_idle' : self.sprite_frames[2], 'left_idle' : self.sprite_frames[3], 
                            'down_walk' : self.sprite_frames[4], 'up_walk' : self.sprite_frames[5], 'right_walk' : self.sprite_frames[6], 'left_walk' : self.sprite_frames[7], 
                            'down_run' : self.sprite_frames[8], 'up_run' : self.sprite_frames[9], 'right_run' : self.sprite_frames[10], 'left_run' : self.sprite_frames[11], 
                            'down_hoe' : self.sprite_frames[12], 'up_hoe' : self.sprite_frames[13], 'right_hoe' : self.sprite_frames[14], 'left_hoe' : self.sprite_frames[15], 
                            'down_axe' : self.sprite_frames[16], 'up_axe' : self.sprite_frames[17], 'right_axe' : self.sprite_frames[18], 'left_axe' : self.sprite_frames[19], 
                            'down_water' : self.sprite_frames[20], 'up_water' : self.sprite_frames[21], 'right_water' : self.sprite_frames[22], 'left_water' : self.sprite_frames[23], }
        print(self.animations['right_water'])
        

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    
    def update(self, dt):
        self.input()
        self.move(dt)