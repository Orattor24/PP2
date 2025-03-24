import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colors = [colorRED, colorBLUE, colorWHITE, colorBLACK]
color_index = 0  # Индекс текущего цвета

LMBpressed = False
THICKNESS = 5
print("Привет. Краткая инструкция. 1 - красный. 2- синий. 3 - белый. 4 - стерка. удачи!")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                pygame.draw.rect(screen, colors[color_index], (event.pos[0], event.pos[1], THICKNESS, THICKNESS))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False





        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)  # Толщина не может быть меньше 1
            if event.key == pygame.K_1:
                color_index = 0  # Красный
            if event.key == pygame.K_2:
                color_index = 1  # Синий
            if event.key == pygame.K_3:
                color_index = 2  # Белый
            if event.key == pygame.K_4:
                color_index = 3  # Чёрный

    pygame.display.flip()
