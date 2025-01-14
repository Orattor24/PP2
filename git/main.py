import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение красного квадрата")

# Начальная позиция и размеры квадрата
square_size = 50
square_x = WIDTH // 2 - square_size // 2
square_y = HEIGHT // 2 - square_size // 2

# NPC параметры
npc_size = 50
npc_x = random.randint(0, WIDTH - npc_size)
npc_y = random.randint(0, HEIGHT - npc_size)

# Скорость движения
speed = 5

# Главный цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение состояния клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed

    # Ограничение движения в пределах окна
    square_x = max(0, min(WIDTH - square_size, square_x))
    square_y = max(0, min(HEIGHT - square_size, square_y))

    # Проверка столкновения
    if (square_x < npc_x + npc_size and
            square_x + square_size > npc_x and
            square_y < npc_y + npc_size and
            square_y + square_size > npc_y):
        # Переместить NPC в случайное место
        npc_x = random.randint(0, WIDTH - npc_size)
        npc_y = random.randint(0, HEIGHT - npc_size)

        # Увеличить размер квадрата
        square_size += 50

    # Рендеринг
    screen.fill(WHITE)  # Белый фон
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    pygame.draw.rect(screen, GREEN, (npc_x, npc_y, npc_size, npc_size))
    if square_size == WIDTH:
        pygame.quit()

    # Рисование глаз на квадрате
    eye_radius = square_size // 10
    eye_offset_x = square_size // 4
    eye_offset_y = square_size // 4

    # Левый глаз
    pygame.draw.circle(screen, BLACK, (square_x + eye_offset_x, square_y + eye_offset_y), eye_radius)
    # Правый глаз
    pygame.draw.circle(screen, BLACK, (square_x + square_size - eye_offset_x, square_y + eye_offset_y), eye_radius)

    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(60)

# Завершение работы Pygame
pygame.quit()
