import pygame

pygame.init()

w, h = 500, 500

white = (255, 255, 255)
red = (255, 0, 0)
screen = pygame.display.set_mode((w, h))

pygame.display.set_caption("шарик")

x = w // 2
y = h // 2
velocity = 20

def draw_ball(x, y):
    pygame.draw.circle(screen, red, (x, y), 25)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= velocity
            elif event.key == pygame.K_DOWN:
                y += velocity
            elif event.key == pygame.K_LEFT:
                x -= velocity
            elif event.key == pygame.K_RIGHT:
                x += velocity

    if x < 25:
        x = 25
    elif x > w - 25:
        x = w - 25
    if y < 25:
        y = 25
    elif y > h - 25:
        y = h - 25

    screen.fill(white)

    draw_ball(x, y)

    pygame.display.update()