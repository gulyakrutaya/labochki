import pygame
from math import cos, sin , pi 

pygame.init()

screen = pygame.display.set_mode((800, 600))
surf = pygame.Surface((700, 600)) # где будем рисовать
buttons = pygame.Surface((100, 240)) # панель кнопок
font = pygame.font.SysFont("Verdana", 15)
cur_color = 'white' # цвет которым рисуем

# штуки и их размеры
commands = {
    'right_triangle': [4, 4, 44, 44],
    'sqr': [52, 4, 44, 44],
    'triangle': [4, 50, 44, 44],
    'rhombus': [52, 50, 44, 44],
    'eraser' : [1000, 1000, 1, 1]
}

# отрисовываю панель
def setsurf():
    surf.fill('black')
    buttons.fill('white')
    pygame.draw.rect(buttons, 'black', (2, 2, 96, 236), 1)
    
    for i in commands:
        pygame.draw.rect(buttons, 'black', commands[i], 1)
        
    tr1 = pygame.image.load("lab9\\right_triangle.png")
    buttons.blit(tr1, (8, 8))
    tr2 = pygame.image.load("lab9\\equilateral-triangle.png")
    buttons.blit(tr2, (8, 55))
    pygame.draw.rect(buttons, 'black', (58, 10, 32, 32), 2)
    rh = pygame.image.load("lab9\\rhombus.png")
    buttons.blit(rh, (56, 58))
    screen.blit(surf, (0, 0))
    screen.blit(buttons, (700, 0))

# расстояние между точками
def get_distance(a,b): 
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

# функция для отрисовки прямоугольного треугольника
def right_triangle(screen, cur, end, d, color): 
    x1, y1, x2, y2 = cur[0], cur[1], end[0], end[1] 
    difx = abs(x1-x2) 
    dify = abs(y1-y2) 
    if x1 <= x2: 
        if y1 < y2: 
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
        else: 
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    
             
    else: 
        if y1 < y2: 
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 + dify), (x2, y2)], d)    
        else: 
            pygame.draw.polygon(screen, color, [(x1, y1), (x1, y1 - dify), (x2, y2)], d)    
# функция для отрисовки равностороннего треугольника
def triangle(color, pos):
    pygame.draw.polygon(surf, color, pos, 3)
# функция для отрисовки квадрата
def square(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    a = abs(x1-x2)
    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x1, y1, a, a), d)
        else:
            pygame.draw.rect(screen, color, (x1, y2, a, a), d)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, a, a), d)
        else:
            pygame.draw.rect(screen, color, (x2, y2, a, a), d)
# функция для отрисовки ромба
def rhombus(color, pos):
        pygame.draw.polygon(surf, color, pos, 3)

last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

di = {
    'right_triangle' : True,
    'sqr': False,
    'triangle': False,
    'rhombus': False,
    'eraser' : False
}

setsurf()
running = True
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # меняем цвета  или выбираем ластик при нажатии на клавиши             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cur_color = 'red'
            if event.key == pygame.K_2:
                cur_color = 'green'
            if event.key == pygame.K_3:
                cur_color = 'blue'
            if event.key == pygame.K_4:
                cur_color = 'white'
            if event.key == pygame.K_5: 
                di['eraser'] = True 
                for k, v in di.items(): 
                    if k != 'eraser': 
                        di[k] = False   
        # при нажатии на область определенной кнопочки меняем значение соответственной команды на True в словаре комманд           
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    di[k] = True
                    for i, j in di.items():
                        if i != k:
                            di[i] = False
                    break
        # запускаем функции соответственных комманд                 
        if di['right_triangle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                right_triangle(surf, last_pos, pos, w, cur_color)
        elif di['sqr'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                square(surf, last_pos, pos, w, cur_color)
        elif di['triangle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                triangle(cur_color,[last_pos, pos,((pos[0] - last_pos[0])*cos(pi/3) - (pos[1] - last_pos[1])*sin(pi/3) + last_pos[0], (pos[0] - last_pos[0])*sin(pi/3) + (pos[1] - last_pos[1])*cos(pi/3) + last_pos[1])])
        elif di['rhombus'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                d = get_distance(last_pos, pos)
                rhombus(cur_color, [last_pos, (last_pos[0] + d, last_pos[1]), (pos[0] + d, pos[1]), pos])
        elif di['eraser'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                pygame.draw.rect(surf, 'black', (x, y, ed, ed))
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(surf, 'black', (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False
    # выделяю красной рамкой выбранную комманду
    for k, v in di.items():
        if v == True:
            pygame.draw.rect(buttons, 'red', commands[k], 1)
        else:
            pygame.draw.rect(buttons, 'black', commands[k], 1)
    
    screen.blit(buttons, (700, 0))
    screen.blit(surf, (0, 0))
    c = font.render('Press:', True, 'black')
    buttons.blit(c, (5, 100))
    r = font.render('1 - Red', True, 'black')
    buttons.blit(r, (5, 120))
    g = font.render('2 - Green', True, 'black')
    buttons.blit(g, (5, 140))
    b = font.render('3 - Blue', True, 'black')
    buttons.blit(b, (5, 160))
    y = font.render('4 - White', True, 'black')
    buttons.blit(y, (5, 180))
    e = font.render('5 - Eraser', True, 'black')
    buttons.blit(e, (5, 200))

    pygame.display.update()