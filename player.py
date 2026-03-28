import pygame

MAX_LIVES = 3
GRAVITY = 0.7
JUMP_FORCE = -14
SHIELD_DURATION = 4000
SLOW_DURATION = 4000


class Player(pygame.sprite.Sprite):
    """Player sprite with jump, lives, shield and slow motion support."""

    def __init__(self, image, start_x, ground_y):
        super().__init__()
        self.base_image = image
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect(midbottom=(start_x, ground_y))
        self.ground_y = ground_y
        self.vel_y = 0
        self.speed = 6
        self.lives = MAX_LIVES
        self.shield_timer = 0
        self.slow_timer = 0
        self.hit_timer = 0

    @property
    def is_invincible(self):
        return self.shield_timer > 0

    @property
    def is_slow(self):
        return self.slow_timer > 0

    def reset(self, start_x, ground_y):
        self.rect.midbottom = (start_x, ground_y)
        self.ground_y = ground_y
        self.vel_y = 0
        self.lives = MAX_LIVES
        self.shield_timer = 0
        self.slow_timer = 0
        self.hit_timer = 0

    def update(self, dt, keys, width, ground_y):
        speed = self.speed * (0.5 if self.is_slow else 1)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += speed

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.vel_y = 0

        self._update_timers(dt)
        self._update_animation()

    def jump(self):
        if self.rect.bottom >= self.ground_y:
            self.vel_y = JUMP_FORCE

    def take_hit(self):
        if self.is_invincible:
            return False
        self.lives -= 1
        self.hit_timer = 800
        return self.lives <= 0

    def apply_powerup(self, powerup_type):
        if powerup_type == 'shield':
            self.shield_timer = SHIELD_DURATION
        elif powerup_type == 'slow':
            self.slow_timer = SLOW_DURATION
        elif powerup_type == 'life':
            self.lives = min(self.lives + 1, MAX_LIVES)

    def _update_timers(self, dt):
        if self.shield_timer > 0:
            self.shield_timer = max(0, self.shield_timer - dt)
        if self.slow_timer > 0:
            self.slow_timer = max(0, self.slow_timer - dt)
        if self.hit_timer > 0:
            self.hit_timer = max(0, self.hit_timer - dt)

    def _update_animation(self):
        self.image = self.base_image.copy()
        if self.is_invincible and (pygame.time.get_ticks() % 300) < 150:
            overlay = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 128))
            self.image.blit(overlay, (0, 0))
        if self.hit_timer > 0:
            overlay = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
            overlay.fill((255, 20, 20, 100))
            self.image.blit(overlay, (0, 0))
