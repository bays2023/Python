import pygame
turn = "X"
fill = (56, 56, 56)
gridArray1 = 0
gridArray2 = 0
gridCollumn = 50
gridRow = 50
winX = 450
winY = 450
gridArray = [["blank", "blank", "blank"], ["blank", "blank", "blank"], ["blank", "blank", "blank"]]
run = True
gridImage = pygame.image.load('Grid.png')
xImage = pygame.image.load('X.png')
yImage = pygame.image.load('Y.png')
turnImage = xImage
clock = pygame.time.Clock()
display = pygame.display.set_mode((winX, winY))
mouse = pygame.mouse
display.fill(fill)
display.blit(gridImage, (50, 50))
pygame.display.update()
pygame.display.set_caption("Tic Tac Toe")
