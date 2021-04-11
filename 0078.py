import pygame  # модуль

sc = pygame.display.set_mode((600, 400))  # задаем экран
x = 0
y = 0
speed = 5
idle = pygame.image.load("game/Individual Sprites/idle.png")  # чтоб стоял
animate = "idle"
animateIndex = 0  # смена кадров
animateRun = [  # кадры
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0001.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0002.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0003.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0003.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0004.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0005.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0006.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0007.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0008.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0009.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0010.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0011.png"),
    pygame.image.load("game/Individual Sprites/Walk/walkcolor0012.png")
]
image = idle

game = True  # активация игры
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()  # проверка на зажатие клавиши
    # чтоб при не нажатии останавливался

    animate="idle"
    if keys[pygame.K_d]:
        animate = "run"
        x += speed
    if keys[pygame.K_a]:  # a_pass
        x -= speed
        animate = "run"
    if keys[pygame.K_w]:  # w_pass
        y -= speed
        animate = "run"
    if keys[pygame.K_s]:  # s_pass
        y += speed
        animate = "run"


    if animate == "idle":
        image = idle
    if animate == "run":
        animateIndex += 1
        if animateIndex == 12:
            animateIndex = 0
        image = animateRun[animateIndex]



    sc.fill((255, 255, 255))  # закраска поля

    sc.blit(image, (x, y))  # смена кадров

    pygame.display.update()
    pygame.time.delay(60)
