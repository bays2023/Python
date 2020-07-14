from varriables import *
pygame.init()
while run:
	clock.tick(30)
	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		display.fill(fill)
		display.blit(gridImage, (50, 50))
		gridArray = [["blank", "blank", "blank"], ["blank", "blank", "blank"], ["blank", "blank", "blank"]]
		turn = "X"
		turnImage = xImage
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousePosition = mouse.get_pos()
			mouseX = mousePosition[0]
			mouseY = mousePosition[1]
			if mouseX >= 50 and mouseX <= 425 and mouseY >= 50 and mouseX <= 425:
				if mouseX >= 50 and mouseX <= 150:
					gridArray2 = 0
					gridRow = 50
					if mouseY >= 50 and mouseY <= 150:
						gridArray1 = 0
						gridCollumn = 50
					if mouseY >= 175 and mouseY <= 275:
						gridArray1 = 1
						gridCollumn = 175
					if mouseY >= 300 and mouseY <= 400:
						gridArray1 = 2
						gridCollumn = 300
				if mouseX >= 175 and mouseX <= 275:
					gridArray2 = 1
					gridRow = 175
					if mouseY >= 50 and mouseY <= 150:
						gridArray1 = 0
						gridCollumn = 50
					if mouseY >= 175 and mouseY <= 275:
						gridArray1 = 1
						gridCollumn = 175
					if mouseY >= 300 and mouseY <= 400:
						gridArray1 = 2
						gridCollumn = 300
				if mouseX >= 300 and mouseX <= 400:
					gridArray2 = 2
					gridRow = 300
					if mouseY >= 50 and mouseY <= 150:
						gridArray1 = 0
						gridCollumn = 50
					if mouseY >= 175 and mouseY <= 275:
						gridArray1 = 1
						gridCollumn = 175
					if mouseY >= 300 and mouseY <= 400:
						gridArray1 = 2
						gridCollumn = 300
				if gridArray[gridArray1][gridArray2] != turn:
					gridArray[gridArray1][gridArray2] = turn
					display.blit(turnImage, (gridRow, gridCollumn))
				print(gridArray)
				if turn == "X":
					turn = "Y"
					turnImage = yImage
				else:
					turn = "X"
					turnImage = xImage
	pygame.display.update()
pygame.quit()
