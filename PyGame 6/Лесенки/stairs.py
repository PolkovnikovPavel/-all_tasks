import pygame
import os
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


class Platform(pygame.sprite.Sprite):
    image = load_image("platform.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Platform.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def set_cor(self, cor):
        self.rect.x, self.rect.y = cor

    def update(self, *args):
        pass


class Stairs(Platform):
    image = load_image("stairs.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Stairs.image
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    image = load_image("player.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.shift_y = 0
        self.visibility = False

    def set_cor(self, cor):
        self.rect.x, self.rect.y = cor
        self.shift_y = 0
        self.visibility = True

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def go_up(self, shift_y):
        if pygame.sprite.spritecollideany(self, stairs_group):
            self.rect.y += shift_y

    def update(self, *args):
        self.shift_y += GRAVITY
        for _ in range(int(self.shift_y)):
            if (not pygame.sprite.spritecollideany(self, platforms) and
                    not pygame.sprite.spritecollideany(self, stairs_group)):
                self.rect.y += 1
            else:
                self.shift_y = 0
        if self.rect.y > height:
            self.shift_y = 0


size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
FPS = 60
GRAVITY = 1
clock = pygame.time.Clock()

platforms = pygame.sprite.Group()
stairs_group = pygame.sprite.Group()
players = pygame.sprite.Group()
player = Player(players)



while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if event.button == 1:
                key = pygame.key.get_pressed()
                if key[pygame.K_LCTRL]:
                    stairs = Stairs(stairs_group)
                    stairs.set_cor((x, y))
                else:
                    platform = Platform(platforms)
                    platform.set_cor((x, y))
            if event.button == 3:
                player.set_cor((x, y))

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        player.rect.x += 2
    if key[pygame.K_LEFT]:
        player.rect.x -= 2
    if key[pygame.K_UP]:
        player.go_up(-2)
    if key[pygame.K_DOWN]:
        player.go_up(2)

    stairs_group.draw(screen)
    platforms.draw(screen)
    if player.visibility:
        players.draw(screen)
        players.update()

    pygame.display.flip()

pygame.quit()
