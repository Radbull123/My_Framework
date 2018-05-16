import pygame, random

size_x = 1240
size_y = 720

pygame.init()
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Forrest Survive")
clock = pygame.time.Clock()
# -----Init for a game--------------------------------------------------
game_over = False

jumping = False
jumping_hight = 400

go_left = False
go_right = False

x = 54
y = 569
y_hero = False

arrows = []
enemy_r = []
enemy_list = []
count_arrows = 50

y_target = False
count_death = []
WHITE = (255, 255, 255)

# -----Var characters---------------------------------------------------

fone_image = pygame.transform.scale(pygame.image.load("fon.png"), (1240, 720))
hero_image = pygame.transform.scale(pygame.image.load('hero2.png'), (110, 111))
arrow_image = pygame.transform.scale(pygame.image.load('arrow.png'), (55, 90))
enemy_r_image = pygame.transform.scale(pygame.image.load('enemy1.png'), (110, 111))
font_txt = pygame.font.SysFont('arrow', 30, True, False)


pygame.mixer.music.load('sound_main.mp3')
pygame.mixer.music.play(-1)

# -----Downloads files--------------------------------------------------

while not game_over:
# ---------second watch--------------------------------------------------
    count_txt = font_txt.render('ARROWS: '+str(count_arrows), False, WHITE)
    count_time = font_txt.render('PASSAGE TIME: {:.0f}'.format(pygame.time.get_ticks()/1000), False, WHITE)
    seconds = 'Your time is: {} seconds'.format(pygame.time.get_ticks()/1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            print seconds
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                go_right = True
            if event.key == pygame.K_LEFT:
                go_left = True
            if event.key == pygame.K_UP and jumping == False and y == 569:
                jumping = True
            if event.key == pygame.K_SPACE:
                count_arrows -= 1
                if count_arrows > 0:
                    arrows.append([x + 110, y])

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                go_right = False
            if event.key == pygame.K_LEFT:
                go_left = False

    if go_right:
        x += 2
        if x > size_x - 110:
            x = size_x - 110
    if go_left:
        x -= 2
        if x < 0:
            x = 0
    if jumping:
        y -= 4
        if y <= jumping_hight:
            jumping = False
    elif jumping == False and y < 569:
        y += 4
# --------------Jump logic & move var--------------------------------------------

    if not any(enemy_r):
        for count in range(random.randrange(1, 15)):
            count = random.randint(1295, 3800)
            if count not in enemy_r:
                enemy_r.append(count)

# --------------Create a new enemys----------------------------------------------
    if count_arrows <= 0:
        count_arrows = 0
    for x_way in range(len(arrows)):
        arrows[x_way][0] += 4
    for arrow in arrows:
        if arrow[0] > 1240:
            arrows.remove(arrow)
        if arrow[1] in range(514, 570):
            y_target = True
        elif arrow[1] in range(0, 514):
            y_target = False
        if y_target:
            for enemy in enemy_r:
                if arrow[0] + 55 in range(enemy, enemy + 8):
                    arrows.remove(arrow)
                    enemy_r.remove(enemy)
# -------------Arrows moves ------------------------------------------------------
    for way in range(len(enemy_r)):
        enemy_r[way] -= 4

    screen.blit(fone_image, [0, 0])

    for enemy in enemy_r:
        if enemy < -110:
            enemy_r.remove(enemy)
        elif enemy in range(x-8, x) and y in range(500, 570):
            print 'You are die!!!', '\n', seconds
            exit()

    screen.blit(hero_image, [x, y])
    for enemy in enemy_r:
        screen.blit(enemy_r_image, pygame.Rect(enemy, 569, 0, 0))

    for arrow in arrows:
        screen.blit(arrow_image, pygame.Rect(arrow[0], arrow[1], 0, 0))
    screen.blit(count_txt, [50, 50])
    screen.blit(count_time, [600, 50])
    pygame.display.update()
    clock.tick(100)
# -----While loop-------------------------------------------------------