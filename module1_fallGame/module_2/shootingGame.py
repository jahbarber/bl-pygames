import pygame
import random

pygame.init()

FPS = 60
clock = pygame.time.Clock()

WIDTH=800
HEIGHT=600

screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")

class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50,30))
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.rect.x += 5

class Bullet(pygame.sprite.Sprite):
        def _init_(self, x, y):
            super()._init_()
            self.image = pygame.Surface((5,10))
            self.image.fill((RED))
            self.rect = self.image.get_rect()
            self.rect.cemter = (x,y)

        def update(self):
            self.rect.y -= 5
            if self.rect.bottom < 0 :
                self.kill()

class Enemy(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface ((50,50))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,750)
        self.rect.y = random.randint(-200, -50)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0,750)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
for hit in hits:
    new_enemy = Enemy()
    all_sprites.add(new_enemy)
    enemies.add(new_enemy)

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()























all_sprites.update()


hits = pygame.sprite.groupcollide(bullets,enemies, True, True)
for hit in hit:
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip







pygame.quit()


