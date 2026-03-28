import random

import pygame


class Obstacle(pygame.sprite.Sprite):
    """Obstacle sprite that falls down the screen at varying speed."""

    TYPES = [
        {'name': 'rock', 'speed': 4, 'scale': 1.0},
        {'name': 'spike', 'speed': 6, 'scale': 1.1},
    ]

    def __init__(self, image, width):
        super().__init__()
        self.definition = random.choice(self.TYPES)
        base_width = int(image.get_width() * self.definition['scale'])
        base_height = int(image.get_height() * self.definition['scale'])
        self.image = pygame.transform.smoothscale(image, (base_width, base_height))
        x = random.randint(0, max(0, width - base_width))
        self.rect = self.image.get_rect(midtop=(x, -base_height))
        self.speed = self.definition['speed']

    def update(self, dt, speed_scale=1.0):
        self.rect.y += int(self.speed * speed_scale * (dt / 16))
        if self.rect.top > 680:
            self.kill()


class PowerUp(pygame.sprite.Sprite):
    """Power-up sprite that the player can collect for bonuses."""

    TYPES = ['shield', 'slow', 'life']

    def __init__(self, image, width):
        super().__init__()
        self.kind = random.choice(self.TYPES)
        self.image = image.copy()
        self.rect = self.image.get_rect(midtop=(random.randint(20, max(20, width - 20)), -34))
        self.speed = 3

    def update(self, dt, speed_scale=1.0):
        self.rect.y += int(self.speed * speed_scale * (dt / 16))
        if self.rect.top > 680:
            self.kill()
