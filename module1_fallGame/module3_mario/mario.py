import pygame
import sys

pygame.init()

h = 800
w =750

screen = pygame.display.set_mode((h,w))
clock = pygame.time.Clock()
screen.fill((255,255,255))

pygame.display.set_caption("Fario")

class Player:
    def _init_(self, x, y):
        self.size = (40,60)
        self.rect = pygame.Rect((x,y), self.size)
        self.position = (100, h-125)
        self.vel = (0,0)
        self.speed = 5
        self.jump = -15
        self.gravity = 1
        self.onGround = False

    def input(self, keys):
        if keys[pygame.K_KEFT]:
            self.vel[0] = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.vel[0] = self.speed
        


        if keys[pygame.K_Space] and self.onGround:
            self.vel[1] = self.jump
            self.onGround = True

    def draw(self,surface, scroll_x):
        pygame.draw.rect(surface(0,0,220, )
                         (self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height))
        

class Enemy:
    def _init_(self,x,y, width = '40', height='40'):
        self.rect = pygame.Rects(x,y,width,height)

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, (0,0,220), (scroll.rect.x - scroll_x, self.rect.y, self))

platforms =[
    pygame.Rect(0, h -100, 2000, 40),
    pygame.Rect(300, h-200, 200, 40),
    pygame.Rect(600, h-300, 200, 40),
    pygame.Rect(900, h-400, 200, 40)
]



player = Player(100, h-150)
enemies = [Enemy(500, h -150), Enemy (800, h - 90), Enemy(1000, h - 90)]
running = True

while running:
    clock.tick(60)
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys= pygame.key.get_pressed()
    player.input(keys)

    player.apply_physics(platforms)

    for plat in platforms:
        pygame.draw.rect(screen,(0,255,0), (plat.x, plat.y, plat.width, plat.height))
                         
    player.draw(screen,scroll_x)

    for plat in platforms:
            plat_rect=plat.copy()

    player.draw(screen)    
    
    pygame.display.flip()