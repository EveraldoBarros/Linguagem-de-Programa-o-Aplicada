import os

import pygame

from assets import get_asset_path


def load_image(filename):
    """Load an image from the assets folder."""
    path = get_asset_path(filename)
    return pygame.image.load(path).convert_alpha()


def load_sound(filename):
    """Load a sound from the assets folder."""
    path = get_asset_path(filename)
    try:
        return pygame.mixer.Sound(path)
    except pygame.error:
        return None


def load_music(filename):
    """Load background music from the assets folder."""
    path = get_asset_path(filename)
    try:
        pygame.mixer.music.load(path)
    except pygame.error:
        pass


def draw_text(surface, text, size, x, y, color=(255, 255, 255), center=False):
    """Render text to the screen with optional centering."""
    font = pygame.font.SysFont(None, size)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(rendered, rect)
    return rect


class Button:
    """Simple button class for clickable menu elements."""

    def __init__(self, text, rect, font_size=28, color=(255, 255, 255), bg_color=(40, 94, 160), border_color=(255, 255, 255)):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.font_size = font_size
        self.color = color
        self.bg_color = bg_color
        self.border_color = border_color
        self.hover_color = (60, 120, 200)

    def draw(self, surface, hover=False):
        color = self.hover_color if hover else self.bg_color
        pygame.draw.rect(surface, self.border_color, self.rect, border_radius=18)
        pygame.draw.rect(surface, color, self.rect.inflate(-8, -8), border_radius=14)
        draw_text(surface, self.text, self.font_size, self.rect.centerx, self.rect.centery, color=self.color, center=True)

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hover(event.pos)
