#включаем модуль
import pygame

#устанавливаем размеры экрана
sc = pygame.display.set_mode((800, 600))
#включаем игру
game = True

#вводим переменные
x = 250
a = 25
y = 20
d = 679#x
b = 20
c = 475#y
в = 20
z = 25
startY = 0
maxJump = 100
playerx = 679
playery = 475
green = 29, 112, 36
darkgreen = 140, 139, 42
speed1 = 15
#когда клавиша отпущена ничего не двигается
d_pass = False
a_pass = False
w_pass = False
s_pass = False
ц_pass = False
ф_pass = False
в_pass = False
ы_pass = False
isJumpUp = False
isJumpDown = False

#загружаем изображение
imageLeft = pygame.image.load("i.png")
#создаем матрицу под карту
lvl = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
)
#делаем карту









lvlx = 0
lvly = 0
#делаем так, чтоб изображение разворачивалось влево и вправо
imageLeft = pygame.transform.scale(imageLeft, (100, 100))
imageRight = pygame.transform.flip(imageLeft, True, False)
image = imageLeft
#делаем так, чтоб изображение разворачивалось влево и вправо
while game:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.unicode == "d":
                image = imageLeft
                d_pass = True
            elif i.unicode == "a":
                image = imageRight
                a_pass = True
            elif i.unicode == "w":
                w_pass = True
            elif i.unicode == "s":
                s_pass = True
            elif i.unicode == "в":
                image = imageLeft
                в_pass = True
            elif i.unicode == "ы":
                ы_pass = True
            elif i.unicode == "ф":
                image = imageRight
                ф_pass = True
            elif i.unicode == "ц":
                ц_pass = True



#делаем так, чтоб при на ненажатии на клавиши изображене недвигалось
        if i.type == pygame.KEYUP:
            if i.unicode == "d":
                d_pass = False
            elif i.unicode == "a":
                a_pass = False
            elif i.unicode == "w":
                w_pass = False
            elif i.unicode == "s":
                s_pass = False
            elif i.unicode == "в":
                в_pass = False
            elif i.unicode == "ы":
                ы_pass = False
            elif i.unicode == "ф":
                ф_pass = False
            elif i.unicode == "ц":
                ц_pass = False
        if i.type == pygame.QUIT:
            game = False








    sc.fill((120, 179, 235))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        d -= speed1
    if keys[pygame.K_d]:
        d += speed1
    if keys[pygame.K_w]:
        if not isJumpUp and not isJumpDown:
            startY = c
            isJumpUp = True


    if isJumpUp:
        c -= speed1

    if isJumpDown:
        c += speed1

    if isJumpUp and c <= startY - maxJump:
        isJumpUp = False
        isJumpDown = True

    if isJumpDown and c >= startY:
        isJumpDown = False



    #задаем скорость
    speed = 10
#задаем в какую сторону должно двигаться изображение при нажатии на клавиши. создаем поля игры


    if s_pass:
        if c <= 495:
            c += speed
        else:
            lvly -= speed

    if a_pass:
        if d >= 5:
            d -= speed
        else:
            lvlx += speed

    if d_pass:
        if d <= 695:
            d += speed
        else:
            lvlx -= speed
    if в_pass:
        if d <= 695:
            d += speed
        else:
            lvlx -= speed

    if ы_pass:
        if c <= 495:
            c += speed
        else:
            lvly += speed
    if ф_pass:
        if d >= 5:
            d -= speed
        else:
            lvlx -= speed

    for i, line in enumerate(lvl):
        for j, block in enumerate(line):
            if block == 0:
                pygame.draw.rect(sc, (green), ((j * z) + lvlx, (i * z) + lvly, z, z))
            if block == 1:
                pygame.draw.rect(sc, (darkgreen), ((j * z) + lvlx, (i * z) + lvly, z, z))

    sc.blit(image, (d, c))
    #частота обновлений экрана
    pygame.display.update()
    pygame.time.delay(100)