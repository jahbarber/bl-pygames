import pygame
import random

# Initialize game -tells computer that the following
# code should be interpreted as a game.
pygame.init()

# Step 1. Set up the display
height = 1000
width = 1200
WHITE = (255, 255, 255)
playerColor = (255,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# this is reusable code that represents our game screen
screen = pygame.display.set_mode((width, height))


# user opens our game
pygame.display.set_caption("Avoid the Falling Objects")

# Set frame rate
clock = pygame.time.Clock()
FPS = 60




class Player:
    def _init_(self):
        self.x = width // 2 # Start in the middle
        self.y = height - 60
        self.playerWidth = 50
        self.playerHeight = 50
        self.playerSpeed = 5 #How fast the player moves

    def move(self,keys):
        if keys[pygame.K_LEFT] and self.x > 0:
        
            self.x -= self.playerSpeed
        if keys[pygame.K_RIGHT] and self.x < width - self.playerWidth:
            self.x += self.playerSpeed

    def draw(self):
        pygame.draw.rect(screen, playerColor(self.x, self.y, self.width , self.height))



class FallingObject:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = -height
        self.width = width
        self.height = height
        self.speed = random.randint(3, 7)

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.y > height

# Game loop
player = Player()
falling_objects = []
score = 0
lives = 3
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    player.move(keys)
    player.draw()

    

#Player movement
 

    # Add falling objects periodically
    if random.randint(1, 30) == 1:  # Lower the number to increase difficulty
        falling_objects.append(FallingObject())

    # Update falling objects
    for obj in falling_objects[:]:
        obj.move()
        obj.draw()

        # Check for collision
        if (obj.x < player.x + player.width and
            obj.x + obj.width > player.x and
            obj.y < player.y + player.height and
            obj.y + obj.height > player.y):
            lives -= 1
            falling_objects.remove(obj)  # Remove object on collision

       

    pygame.display.update()  # Refresh screen

pygame.quit()