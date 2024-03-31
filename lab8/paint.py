import pygame
pygame.init() 

painting = []

clock = pygame.time.Clock() 

activeColor = (0, 0, 0)
activeShape = 0

w, h = 800, 600

screen = pygame.display.set_mode((w, h)) 

pygame.display.set_caption("рисовашки")

def drawDisplay():
    # Draw Display
    pygame.draw.rect(screen, 'gray', [0, 0, w, 100])

    # Draw Line separator
    pygame.draw.line(screen, 'black', [0, 100], [w, 100]) 
    rect = [pygame.draw.rect(screen, 'black', [10, 10, 80, 80]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 60, 60])
    circ = [pygame.draw.rect(screen, 'black', [100, 10, 80, 80]), 1]
    pygame.draw.circle(screen, 'white', [140, 50], 30)

    # draw colors
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)] 
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)] 
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)] 
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)] 
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)] 
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)] 

    # draw eraser
    eraser = [pygame.draw.rect(screen, (255, 255, 255), [w - 150, 20, 25, 25]), (255, 255, 255)] 
    return [blue, red, green, yellow, black, purple, eraser], [rect, circ]

def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])

def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30]) # Draw
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)

run = True
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shape:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]
    
    screen.fill('white') 
    colors, shape = drawDisplay() # Draw Display

    mouse = pygame.mouse.get_pos() # Get Mouse Position
    draw()
    
    click = pygame.mouse.get_pressed()[0] # Get Mouse Button Pressed
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) # Add Mouse Position to List
    drawPaint(painting)

    pygame.display.flip() 
    clock.tick(60) 