import math
import os
import struct
import wave

import pygame

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')


def get_asset_path(filename):
    """Return the absolute path for an asset file."""
    return os.path.join(ASSETS_DIR, filename)


def ensure_assets():
    """Create the asset folder and files if they do not already exist."""
    os.makedirs(ASSETS_DIR, exist_ok=True)
    pygame.init()
    _create_image('background.png', 800, 600, _draw_background)
    _create_image('player.png', 56, 72, _draw_player)
    _create_image('obstacle.png', 48, 48, _draw_obstacle)
    _create_image('powerup.png', 34, 34, _draw_powerup)
    _create_image('button.png', 240, 70, _draw_button)
    _create_image('screenshot.png', 800, 450, _draw_screenshot)
    _create_wav('jump.wav', 0.14, 880, 0.9)
    _create_wav('hit.wav', 0.4, 220, 0.7, frequency_mod=-8)
    _create_wav('power.wav', 0.3, 660, 0.85)
    _create_music('music.wav')


def _create_image(filename, width, height, draw_func):
    path = get_asset_path(filename)
    if os.path.exists(path):
        return
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    draw_func(surface)
    pygame.image.save(surface, path)


def _draw_background(surface):
    surface.fill((40, 94, 160))
    for y in range(surface.get_height()):
        blend = y / surface.get_height()
        color = (
            int(40 + blend * 80),
            int(94 + blend * 60),
            int(160 + blend * 40),
        )
        pygame.draw.line(surface, color, (0, y), (surface.get_width(), y))
    pygame.draw.rect(surface, (38, 44, 63), (0, surface.get_height() - 130, surface.get_width(), 130))
    for x in range(0, surface.get_width(), 60):
        pygame.draw.ellipse(surface, (61, 70, 96), (x - 20, surface.get_height() - 50, 120, 50))


def _draw_player(surface):
    surface.fill((0, 0, 0, 0))
    body = pygame.Rect(14, 24, 28, 40)
    pygame.draw.rect(surface, (68, 156, 239), body, border_radius=12)
    pygame.draw.circle(surface, (255, 240, 120), (28, 18), 18)
    pygame.draw.circle(surface, (24, 24, 30), (24, 16), 4)
    pygame.draw.circle(surface, (24, 24, 30), (36, 16), 4)
    pygame.draw.rect(surface, (28, 34, 44), (20, 44, 4, 14), border_radius=3)
    pygame.draw.rect(surface, (28, 34, 44), (32, 44, 4, 14), border_radius=3)
    pygame.draw.line(surface, (255, 255, 255), (20, 56), (36, 56), 3)


def _draw_obstacle(surface):
    surface.fill((0, 0, 0, 0))
    pygame.draw.rect(surface, (222, 83, 49), (0, 8, 48, 40), border_radius=10)
    pygame.draw.polygon(surface, (242, 193, 75), [(4, 10), (14, 0), (26, 12), (38, 0), (44, 10)])
    pygame.draw.circle(surface, (209, 46, 46), (14, 28), 8)
    pygame.draw.circle(surface, (209, 46, 46), (34, 30), 8)


def _draw_powerup(surface):
    surface.fill((0, 0, 0, 0))
    colors = [(255, 215, 0), (255, 240, 120), (195, 70, 255)]
    center = (surface.get_width() // 2, surface.get_height() // 2)
    for radius, color in zip((14, 10, 6), colors):
        pygame.draw.circle(surface, color, center, radius)
    for i in range(6):
        angle = math.radians(60 * i)
        end = (
            center[0] + int(math.cos(angle) * 16),
            center[1] + int(math.sin(angle) * 16),
        )
        pygame.draw.line(surface, (255, 255, 255), center, end, 3)


def _draw_button(surface):
    surface.fill((0, 0, 0, 0))
    pygame.draw.rect(surface, (255, 255, 255), (0, 0, surface.get_width(), surface.get_height()), border_radius=18)
    pygame.draw.rect(surface, (40, 94, 160), (8, 8, surface.get_width() - 16, surface.get_height() - 16), border_radius=14)


def _draw_screenshot(surface):
    surface.fill((40, 94, 160))
    pygame.draw.rect(surface, (111, 171, 216), (36, 180, 728, 214), border_radius=22)
    pygame.draw.rect(surface, (68, 156, 239), (52, 210, 700, 140), border_radius=18)
    pygame.draw.circle(surface, (255, 240, 120), (180, 285), 36)
    pygame.draw.rect(surface, (68, 156, 239), (160, 318, 40, 55), border_radius=10)
    pygame.draw.rect(surface, (68, 156, 239), (200, 318, 40, 55), border_radius=10)
    pygame.draw.circle(surface, (255, 255, 255), (175, 280), 5)
    pygame.draw.circle(surface, (255, 255, 255), (205, 280), 5)
    pygame.draw.line(surface, (255, 255, 255), (170, 310), (210, 310), 4)
    for i in range(4):
        x = 388 + i * 110
        pygame.draw.rect(surface, (222, 83, 49), (x, 320, 60, 60), border_radius=12)
    pygame.draw.polygon(surface, (255, 215, 0), [(660, 250), (700, 280), (620, 280)])


def _create_wav(filename, duration, frequency, volume, frequency_mod=0):
    path = get_asset_path(filename)
    if os.path.exists(path):
        return
    sample_rate = 44100
    amplitude = int(32767 * volume)
    count = int(duration * sample_rate)
    with wave.open(path, 'w') as wave_file:
        wave_file.setnchannels(1)
        wave_file.setsampwidth(2)
        wave_file.setframerate(sample_rate)
        samples = bytearray()
        for i in range(count):
            t = i / sample_rate
            freq = frequency + frequency_mod * (t / duration)
            value = int(amplitude * math.sin(2 * math.pi * freq * t))
            samples.extend(struct.pack('<h', value))
        wave_file.writeframes(bytes(samples))


def _create_music(filename):
    path = get_asset_path(filename)
    if os.path.exists(path):
        return
    sample_rate = 44100
    amplitude = int(32767 * 0.4)
    duration = 12.0
    notes = [440, 440, 493, 523, 587, 523, 493, 440, 392, 392, 440, 392, 349, 330]
    with wave.open(path, 'w') as music_file:
        music_file.setnchannels(1)
        music_file.setsampwidth(2)
        music_file.setframerate(sample_rate)
        frames = bytearray()
        for index in range(int(sample_rate * duration)):
            t = index / sample_rate
            note = notes[int((t * 2) % len(notes))]
            value = int(amplitude * math.sin(2 * math.pi * note * t) * (0.5 + 0.5 * math.sin(0.5 * t)))
            frames.extend(struct.pack('<h', value))
        music_file.writeframes(bytes(frames))
