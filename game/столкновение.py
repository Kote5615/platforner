# включаем модуль
import pygame

speed = 10
playerx = 1660
playery = 770
lvlx = 0
lvly = 0

z = 64
i = 30
speed1 = 15
startY = 0
maxJump = 100
isJumpUp = False
isJumpDown = False
# устанавливаем размеры экрана
sc = pygame.display.set_mode((1800, 900))

# загружаем изображение
heroImage = pygame.image.load("i.png")
block = pygame.image.load("1.png")
block = pygame.transform.scale(block, (80, 30))
heroImage = pygame.transform.scale(heroImage, (100, 100))

lvl = (

    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

)

# включаем игру
game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    sc.fill((120, 179, 235))
    for y, line in enumerate(lvl):
        for x, typ in enumerate(line):

            if typ == 1:
                pygame.draw.rect(sc, (0, 0, 0), (x * z + lvlx, y * z + lvly, z, z))
    keys = pygame.key.get_pressed()


    x = (keys[pygame.K_a] * -1 * speed) + (keys[pygame.K_d] * speed)
    y = (keys[pygame.K_s] * speed)

    playerx += x
    playery += y

    if keys[pygame.K_w]:
        if not isJumpUp and not isJumpDown:
            startY = playery
            isJumpUp = True

    if isJumpUp:
        playery -= speed1

    if isJumpDown:
        playery += speed1

    if isJumpUp and playery <= startY - maxJump:
        isJumpUp = False
        isJumpDown = True

    if isJumpDown and playery >= startY:
        isJumpDown = False

    block1 = sc.blit(heroImage, (playerx, playery))



    block2 = pygame.draw.rect(sc, (13, 112, 28), (0, 0, 1800, 30))
    block3 = pygame.draw.rect(sc, (13, 112, 28), (0, 0, 30, 900))
    block4 = pygame.draw.rect(sc, (13, 112, 28), (1770, 0, 30, 900))
    block5 = pygame.draw.rect(sc, (13, 112, 28), (0, 870, 1800, 30))




    col = block1.colliderect(block2)
    col1 = block1.colliderect(block3)
    col2 = block1.colliderect(block4)
    col3 = block1.colliderect(block5)



    if col:
        playerx += x * -1
        playery += y * -1
    if col1:
        playerx += x * -1
        playery += y * -1
    if col2:
        playerx += x * -1
        playery += y * -1
    if col3:
        playerx += x * -1
        playery += y * -1



    # частота обновлений экрана
    pygame.display.update()
    pygame.time.delay(100)
