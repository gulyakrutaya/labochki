import pygame
from pygame.locals import *
import random, time

pygame.init()

fps=pygame.time.Clock()


#basic variables
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

w, h = 400, 600
player_speed = 5
enemy_speed = 5
score = 0
coin = 0

#font variables
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)

#road image
background = pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\AnimatedStreet.png")

#background music
music="C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\background.wav"
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

#screen
screen=pygame.display.set_mode((w, h))
screen.fill(white)
pygame.display.set_caption("форсаж")


#bunch of classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-player_speed, 0)
        if self.rect.right < w:       
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(player_speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40), 0)
    
    def move(self):
        global score
        self.rect.move_ip(0, enemy_speed)
        if self.rect.top > h:
            score +=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), 0)

    def move(self):
        self.rect.move_ip(0, player_speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)

P1 = Player()
E1 = Enemy()
C1 = Coin()

#sprite coca cola
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#чтоб злодеи врум врум
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

run=True

#start
while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run=False

        #vroooom
        if event.type == INC_SPEED:
              enemy_speed += 0.5
    
    #выводим текст на экран
    screen.blit(background, (0, 0))
    scores = font_small.render("Score:"+str(score), True, black)
    coin_scores = font_small.render("Coins:"+str(coin), True, green)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (300, 10))
    
    #making cars and coin move
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #if ДТП occured
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:\\Users\\gulbe\\OneDrive\\Рабочий стол\\PP2\\lab8\\crash.wav').play()
        screen.fill(red)
        screen.blit(game_over, (20, 250))
        screen.blit(scores, (165, 330))
        screen.blit(coin_scores, (165, 350))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        run = False
    
    #getting rich
    if pygame.sprite.spritecollideany(P1, coins):
        coin += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, w - 40), 0)

    #enemies not getting rich       
    if pygame.sprite.spritecollideany(C1, enemies):
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, w - 40), 0)

    pygame.display.update()
    fps.tick(60)