import pygame

def create_frames(spritesheet, rows, columns):
    sprite_sheet = pygame.image.load(spritesheet).convert_alpha()
    frame_width = int(sprite_sheet.get_width() / columns)
    frame_height = int(sprite_sheet.get_height() / rows)
    animations = []
    for y in range(0, rows):
        current_animation = []
        for x in range(0, columns):
            frame = sprite_sheet.subsurface(pygame.Rect(x * frame_width, y * frame_height, frame_width, frame_height))
            current_animation.append(frame)
        animations.append(current_animation)
    return animations
