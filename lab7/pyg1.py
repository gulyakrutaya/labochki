import datetime
import pygame

pygame.init()


size = w , h = 800, 800
middle = w//2 , h//2
r = 1000

angle1=0
amgle2=0

screen=pygame.display.set_mode(size)

c=pygame.time.Clock()

pygame.display.set_caption("yay")

clock=pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\mclock.png")

min=pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\mrh.png").convert_alpha()
minrect=min.get_rect()

sec=pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\mlh.png").convert_alpha()
secrect=sec.get_rect()

minrect.center=secrect.center=middle

pygame.display.set_icon(pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\mickeyclock.jpeg"))

run=True

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    now=datetime.datetime.now().time()
    minute=now.minute
    second=now.second

    angle1=-minute*6+84
    rot1=pygame.transform.rotate(min, angle1)
    rect1=rot1.get_rect()
    rect1.center=minrect.center

    angle2=-second*6-282
    rot2=pygame.transform.rotate(sec, angle2)
    rect2=rot2.get_rect()
    rect2.center=secrect.center

    screen.blit(clock, (0, 0))
    screen.blit(rot1, rect1)
    screen.blit(rot2, rect2)

    pygame.display.flip()
    c.tick(60)