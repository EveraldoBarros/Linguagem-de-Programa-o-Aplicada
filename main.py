import random
import sys

import pygame

from assets import ensure_assets
from obstacle import Obstacle, PowerUp
from player import Player
from utils import Button, draw_text, load_image, load_music, load_sound

WIDTH = 800
HEIGHT = 600
FPS = 60
GROUND_Y = 520
SPAWN_INTERVAL = 700
POWERUP_INTERVAL = 5000
MAX_OBSTACLE_SPEED = 10


def start_game(player, obstacles, powerups):
    """Reset the game state for a new play session."""
    obstacles.empty()
    powerups.empty()
    player.reset(WIDTH // 2, GROUND_Y)
    return 0, 0, 0, 0


def draw_hud(screen, score, time_survived, player):
    """Draw the heads-up display with score, lives and active bonuses."""
    draw_text(screen, f'Pontuação: {score}', 24, 18, 14)
    draw_text(screen, f'Tempo: {int(time_survived)}s', 24, 18, 42)
    draw_text(screen, f'Vidas: {player.lives}', 24, 18, 70)
    if player.is_invincible:
        draw_text(screen, 'INVENCÍVEL', 24, WIDTH - 170, 14, color=(255, 230, 120))
    if player.is_slow:
        draw_text(screen, 'SLOW MOTION', 24, WIDTH - 210, 42, color=(160, 220, 255))


def draw_menu(screen, title, subtitle, buttons, background):
    """Draw the main menu screen with a background and buttons."""
    screen.blit(background, (0, 0))
    draw_text(screen, title, 56, WIDTH // 2, 120, center=True)
    draw_text(screen, subtitle, 24, WIDTH // 2, 190, center=True)
    for button in buttons:
        button.draw(screen, button.is_hover(pygame.mouse.get_pos()))
    draw_text(screen, 'Clique no botão ou pressione ENTER para iniciar.', 20, WIDTH // 2, 520, center=True)
    pygame.display.flip()


def draw_pause(screen, resume_button, menu_button):
    """Draw the pause overlay and buttons."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((10, 10, 20, 180))
    screen.blit(overlay, (0, 0))
    draw_text(screen, 'PAUSADO', 64, WIDTH // 2, 170, center=True)
    draw_text(screen, 'Pressione P ou clique para continuar.', 22, WIDTH // 2, 240, center=True)
    resume_button.draw(screen, resume_button.is_hover(pygame.mouse.get_pos()))
    menu_button.draw(screen, menu_button.is_hover(pygame.mouse.get_pos()))
    pygame.display.flip()


def draw_game_over(screen, score, time_survived, retry_button, menu_button):
    """Draw the game over screen with final score and buttons."""
    screen.fill((18, 18, 32))
    draw_text(screen, 'FIM DE JOGO', 64, WIDTH // 2, 120, center=True)
    draw_text(screen, f'Pontuação final: {score}', 32, WIDTH // 2, 220, center=True)
    draw_text(screen, f'Tempo de sobrevivência: {int(time_survived)}s', 28, WIDTH // 2, 270, center=True)
    draw_text(screen, 'Colete escudos e power-ups para durar mais.', 20, WIDTH // 2, 310, center=True)
    retry_button.draw(screen, retry_button.is_hover(pygame.mouse.get_pos()))
    menu_button.draw(screen, menu_button.is_hover(pygame.mouse.get_pos()))
    pygame.display.flip()


def main():
    ensure_assets()
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    except pygame.error:
        print('Atenção: mixer de áudio não pôde ser inicializado.')

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Demo Game - Linguagem de Programação Aplicada')
    clock = pygame.time.Clock()

    background = load_image('background.png')
    player_image = load_image('player.png')
    obstacle_image = load_image('obstacle.png')
    powerup_image = load_image('powerup.png')

    jump_sound = load_sound('jump.wav')
    hit_sound = load_sound('hit.wav')
    power_sound = load_sound('power.wav')
    load_music('music.wav')
    try:
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
    except pygame.error:
        pass

    player = Player(player_image, WIDTH // 2, GROUND_Y)
    obstacles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(player)

    buttons = {
        'start': Button('JOGAR', (WIDTH // 2 - 120, 310, 240, 70)),
        'exit': Button('SAIR', (WIDTH // 2 - 120, 400, 240, 70)),
    }
    pause_buttons = {
        'resume': Button('CONTINUAR', (WIDTH // 2 - 120, 300, 240, 70)),
        'menu': Button('MENU', (WIDTH // 2 - 120, 390, 240, 70)),
    }
    game_over_buttons = {
        'retry': Button('REINICIAR', (WIDTH // 2 - 260, 380, 220, 70)),
        'menu': Button('MENU', (WIDTH // 2 + 40, 380, 220, 70)),
    }

    state = 'menu'
    score = 0
    time_survived = 0
    spawn_timer = 0
    powerup_timer = 0
    obstacle_speed_scale = 1.0

    while True:
        dt = clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if state == 'menu' and event.key == pygame.K_RETURN:
                    state = 'playing'
                    score, time_survived, spawn_timer, powerup_timer = start_game(player, obstacles, powerups)
                    all_sprites = pygame.sprite.Group(player)
                elif state == 'playing':
                    if event.key == pygame.K_SPACE:
                        player.jump()
                        if jump_sound:
                            jump_sound.play()
                    if event.key == pygame.K_p:
                        state = 'pause'
                elif state == 'pause' and event.key == pygame.K_p:
                    state = 'playing'
                elif state == 'game_over' and event.key == pygame.K_RETURN:
                    state = 'playing'
                    score, time_survived, spawn_timer, powerup_timer = start_game(player, obstacles, powerups)
                    all_sprites = pygame.sprite.Group(player)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if state == 'menu':
                    if buttons['start'].is_hover(mouse_pos):
                        state = 'playing'
                        score, time_survived, spawn_timer, powerup_timer = start_game(player, obstacles, powerups)
                        all_sprites = pygame.sprite.Group(player)
                    elif buttons['exit'].is_hover(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif state == 'pause':
                    if pause_buttons['resume'].is_hover(mouse_pos):
                        state = 'playing'
                    elif pause_buttons['menu'].is_hover(mouse_pos):
                        state = 'menu'
                elif state == 'game_over':
                    if game_over_buttons['retry'].is_hover(mouse_pos):
                        state = 'playing'
                        score, time_survived, spawn_timer, powerup_timer = start_game(player, obstacles, powerups)
                        all_sprites = pygame.sprite.Group(player)
                    elif game_over_buttons['menu'].is_hover(mouse_pos):
                        state = 'menu'

        if state == 'menu':
            draw_menu(
                screen,
                'RUNNER STAR',
                'Desvie, colete e sobrevive em fases cada vez mais rápidas.',
                buttons.values(),
                background,
            )
            continue

        if state == 'pause':
            screen.blit(background, (0, 0))
            draw_hud(screen, score, time_survived, player)
            draw_pause(screen, pause_buttons['resume'], pause_buttons['menu'])
            continue

        if state == 'playing':
            spawn_timer += dt
            powerup_timer += dt
            if spawn_timer > SPAWN_INTERVAL:
                spawn_timer = 0
                obstacle = Obstacle(obstacle_image, WIDTH)
                obstacles.add(obstacle)
                all_sprites.add(obstacle)

            if powerup_timer > POWERUP_INTERVAL:
                powerup_timer = 0
                powerup = PowerUp(powerup_image, WIDTH)
                powerups.add(powerup)
                all_sprites.add(powerup)

            if keys[pygame.K_SPACE]:
                player.jump()

            player.update(dt, keys, WIDTH, GROUND_Y)
            difficulty_scale = min(MAX_OBSTACLE_SPEED, 1 + time_survived / 15)
            speed_scale = difficulty_scale * (0.65 if player.is_slow else 1.0)
            for obstacle in obstacles:
                obstacle.update(dt, speed_scale)
            for powerup in powerups:
                powerup.update(dt, speed_scale)

            collisions = pygame.sprite.spritecollide(player, obstacles, False)
            if collisions:
                if player.is_invincible:
                    for obstacle in collisions:
                        obstacle.kill()
                elif player.take_hit():
                    if hit_sound:
                        hit_sound.play()
                    state = 'game_over'
                else:
                    if hit_sound:
                        hit_sound.play()
                    for obstacle in collisions:
                        obstacle.kill()

            power_hits = pygame.sprite.spritecollide(player, powerups, True)
            for power_up in power_hits:
                player.apply_powerup(power_up.kind)
                if power_sound:
                    power_sound.play()

            score += int(dt / 10)
            time_survived += dt / 1000.0
            obstacle_speed_scale = min(MAX_OBSTACLE_SPEED, 1 + time_survived / 15)

            screen.blit(background, (0, 0))
            pygame.draw.rect(screen, (46, 84, 122), (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))
            draw_hud(screen, score, time_survived, player)
            all_sprites.draw(screen)
            if player.is_invincible:
                pygame.draw.circle(screen, (255, 255, 255, 80), player.rect.center, 52, width=4)
            if player.is_slow:
                draw_text(screen, 'EFEITO LENTO ATIVO', 22, WIDTH // 2, 110, color=(255, 255, 200), center=True)
            pygame.display.flip()
            continue

        if state == 'game_over':
            draw_game_over(screen, score, time_survived, game_over_buttons['retry'], game_over_buttons['menu'])
            continue


if __name__ == '__main__':
    main()
