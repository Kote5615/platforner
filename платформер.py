import pygame

sc = pygame.display.set_mode((800, 800))

playerX = 100
playerY = 500
x = 100
y = 500
speed = 5500
upal = 0
maxJump = 100
startY = 0
isJumpUp = False
isJumpDown = False

stay = pygame.image.load("спрайт/начальное положение.png")
stay = pygame.transform.scale(stay, (100, 100))
stayRight = pygame.transform.flip(stay, True, False)

animate = "stay"




animateRun = [
    pygame.image.load("спрайт/ходьба 5 .png"),
    pygame.image.load("спрайт/ходьба 6.png"),
    pygame.image.load("спрайт/ходьба 1.png"),
    pygame.image.load("спрайт/ходьба 2.png"),
    pygame.image.load("спрайт/ходьба 4.png"),
]


highJump = pygame.image.load("спрайт/великие татары/прыжок 1.png")
LowJump = pygame.image.load("спрайт/великие татары/прыжок 4.png")



for index in range(len(animateRun)):
    animateRun[index] = pygame.transform.scale(animateRun[index], (100, 100))
highJump = pygame.transform.scale(highJump, (100, 100))
LowJump = pygame.transform.scale(LowJump, (100, 100))

animateIndex = 0
animate1 = 0

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    sc.fill((255, 255, 255))


    #гравитация
    if y >=500:
        y = 500

    keys = pygame.key.get_pressed()
    animate = "stay"
    if keys[pygame.K_d]:
        x += speed
        animate = "run"

    if keys[pygame.K_a]:
        x -= speed
        animate = "run"
    if keys[pygame.K_SPACE]:
        if not isJumpUp and not isJumpDown:
            startY = y
            isJumpUp = True

    if isJumpUp:
        y -= 15
        animate = "jump"
    if isJumpDown:
        y += 25
        animate = "jump2"
    if isJumpUp and y <= startY - maxJump:
        isJumpUp = False
        isJumpDown = True

    if isJumpDown and y >= startY:
        isJumpDown = False

    if animate == "stay":
        image = stay
        speed = 0
    if animate == "stayRight":
        image = stayRight
    if animate == "run":
        speed = 10
        animateIndex += 1
        if animateIndex == 4:
            animateIndex = 0
        image = animateRun[animateIndex]
    if animate == "jump":
        image = highJump
    if animate == "jump2":
        image = LowJump






    sc.blit(image, (x, y))

    pygame.display.update()
    pygame.time.delay(100)
