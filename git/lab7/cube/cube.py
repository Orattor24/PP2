import pygame

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Начальные координаты и радиус шара
x, y = 50, 50
radius = 25
speed = 20

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем состояние клавиш
    pressed = pygame.key.get_pressed()

    # Обновляем координаты с учетом границ экрана
    if pressed[pygame.K_UP] and y - speed - radius >= 0:
        y -= speed
    if pressed[pygame.K_DOWN] and y + speed + radius <= HEIGHT:
        y += speed
    if pressed[pygame.K_LEFT] and x - speed - radius >= 0:
        x -= speed
    if pressed[pygame.K_RIGHT] and x + speed + radius <= WIDTH:
        x += speed

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
