import pygame
import os
import random

pygame.init()

# Game Configuration
gameWidth = 640
gameHeight = 640
picSize = 64
gameColumns = 5
gameRows = 4
padding = 10
leftMargin = (gameWidth - ((picSize + padding) * gameColumns)) // 2
topMargin = (gameHeight - ((picSize + padding) * gameRows)) // 2
WHITE = (255, 255, 255)
GRAY = (160, 160, 160)
BLACK = (0, 0, 0)
selection1 = None
selection2 = None

# Set up screen
screen = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Matching Game')

# Load background (optional)
bgImage = pygame.Surface((gameWidth, gameHeight))
bgImage.fill((20, 20, 60))
bgImageRect = bgImage.get_rect()

# Load 5 unique image names
image_files = [f for f in os.listdir('images/') if f.endswith('.jpg')][:10]
memoryPictures = [img.split('.')[0] for img in image_files]

# Create 5 pairs, pad rest with None to fill 100 grid cells
playable_pics = memoryPictures * 2
while len(playable_pics) < gameColumns * gameRows:
    playable_pics.append(None)
random.shuffle(playable_pics)

# Load images or create placeholder blocks
memPics = []
memPicsRect = []
hiddenImages = []

for index in range(gameColumns * gameRows):
    item = playable_pics[index]
    if item is not None:
        image = pygame.image.load(f'images/{item}.jpg')
        image = pygame.transform.scale(image, (picSize, picSize))
    else:
        image = pygame.Surface((picSize, picSize))
        image.fill(GRAY)
    memPics.append(image)

    col = index % gameColumns
    row = index // gameColumns
    rect = pygame.Rect(
        leftMargin + (picSize + padding) * col,
        topMargin + (picSize + padding) * row,
        picSize,
        picSize
    )
    memPicsRect.append(rect)
    hiddenImages.append(False)

# Game loop
gameLoop = True
while gameLoop:
    screen.blit(bgImage, bgImageRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(memPicsRect):
                if rect.collidepoint(event.pos) and playable_pics[i] is not None and not hiddenImages[i]:
                    if selection1 is None:
                        selection1 = i
                        hiddenImages[i] = True
                    elif selection2 is None and i != selection1:
                        selection2 = i
                        hiddenImages[i] = True

    # Draw cards
    for i in range(len(memPics)):
        if hiddenImages[i] or playable_pics[i] is None:
            screen.blit(memPics[i], memPicsRect[i])
        else:
            pygame.draw.rect(screen, WHITE, memPicsRect[i])

    pygame.display.update()

    # Match logic
    if selection1 is not None and selection2 is not None:
        pygame.time.wait(1000)
        if playable_pics[selection1] != playable_pics[selection2]:
            hiddenImages[selection1] = False
            hiddenImages[selection2] = False
        selection1 = selection2 = None

    # Check win (ignore blanks)
    matched = all(hiddenImages[i] for i in range(len(hiddenImages)) if playable_pics[i] is not None)
    if matched:
        pygame.time.wait(2000)
        gameLoop = False

pygame.quit()
