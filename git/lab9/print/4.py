import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))  # Фон делаем белым

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
    """Создаёт список точек для рисования рамки прямоугольника."""
    left = min(x1, x2)
    top = min(y1, y2)
    right = max(x1, x2)
    bottom = max(y1, y2)

    return [
        (left, top),    # Левый верхний
        (right, top),   # Правый верхний
        (right, bottom),  # Правый нижний
        (left, bottom),  # Левый нижний
        (left, top)     # Замыкаем контур
    ]


while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                screen.blit(base_layer, (0, 0))  # Восстанавливаем предыдущее изображение
                currX = event.pos[0]
                currY = event.pos[1]
                points = calculate_rect(prevX, prevY, currX, currY)
                pygame.draw.lines(screen, colorWHITE, True, points, 2)  # Белая рамка
                pygame.draw.rect(screen, colors[color_index], pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1])), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            points = calculate_rect(prevX, prevY, currX, currY)
            pygame.draw.lines(screen, colorWHITE, True, points, 2)  # Белая рамка
            pygame.draw.rect(screen, colors[color_index], pygame.Rect(points[0], (points[2][0] - points[0][0], points[2][1] - points[0][1])), THICKNESS)
            base_layer.blit(screen, (0, 0))  # Сохраняем изменения

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
    clock.tick(60)

