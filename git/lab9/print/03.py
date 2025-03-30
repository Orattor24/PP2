import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colors = [colorRED, colorBLUE, colorWHITE, colorBLACK]
color_index = 0  # Индекс текущего цвета

clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5

currX = 0
currY = 0
done = True
prevX = 0
prevY = 0

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

running = False

while done:

    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]
                pygame.draw.rect(screen, colors[color_index], calculate_rect(prevX, prevY, currX, currY), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            pygame.draw.rect(screen, colors[color_index], calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            base_layer.blit(screen, (0, 0))




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

    # pygame.draw.line(screen, colorRED, (prevX, prevY), (currX, currY), THICKNESS)

    pygame.display.flip()
    clock.tick(60)