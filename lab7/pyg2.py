import pygame
pygame.init()

sp = "C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\spongebob-squarepants-closing-theme.mp3"
wrrrkk = "C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\Rihanna feat. Drake - Work.mp3"
motivaska = "C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\motivational-day-112790.mp3"

sc = pygame.display.set_mode((700, 700))
pygame.display.set_caption("musi-zuzi")
clock = pygame.time.Clock()
index=0

musiccaa = [sp, wrrrkk, motivaska]
pygame.mixer.music.load(musiccaa[index])
pygame.mixer.music.play(0)

kotik = pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab7\\Head-cat.jpeg")

sc.blit(kotik, (0, 0))
play = False
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
                if play:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(musiccaa):
                    index = 0
                pygame.mixer.music.load(musiccaa[index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musiccaa)-1
                pygame.mixer.music.load(musiccaa[index])
                pygame.mixer.music.play()


    pygame.display.flip()
    clock.tick(60)