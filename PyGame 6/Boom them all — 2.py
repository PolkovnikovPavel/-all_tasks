import pygame
import os
import random
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join(name)
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self):
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.w)
        self.rect.y = random.randrange(height - self.rect.h)

    def add_group(self, group):
        super().__init__(group)

    def update(self, *args):
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and
           self.rect.collidepoint(args[0].pos)):
            self.image = self.image_boom


size = width, height = 500, 500
screen = pygame.display.set_mode(size)

running = True
FPS = 60
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
for _ in range(10):
    bomb = Bomb()
    x = pygame.sprite.spritecollideany(bomb, all_sprites)
    while pygame.sprite.spritecollideany(bomb, all_sprites):
        bomb = Bomb()
    bomb.add_group(all_sprites)


while running:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
